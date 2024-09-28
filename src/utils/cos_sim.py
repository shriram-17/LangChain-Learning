import numpy as np
from src.db.db_connection import products_collection
from scipy.spatial.distance import cosine

def vector_search(query_embedding, selected_product_name, n=5):
    """
    Perform a vector similarity search using cosine similarity.
    
    :param query_embedding: The query vector (must be 382-dimensional)
    :param selected_product_name: The name of the selected product (used to exclude from the results)
    :param n: Number of similar products to return
    :return: List of similar products
    """
   
    query_embedding = np.array(query_embedding)
    
    
    all_products = list(products_collection.find({}, {'name': 1, 'type': 1, 'price': 1,'description':1,'store_name': 1, 'embedding': 1}))

    similarities = []
    for product in all_products:
        product_embedding = np.array(product['embedding'])
        similarity = 1 - cosine(query_embedding, product_embedding)  # Convert distance to similarity
        
        # Exclude the selected product from the similarity results
        if product['name'] != selected_product_name:
            similarities.append((product, similarity))
    
    # Sort by similarity (descending) and get top n
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_similar = similarities[:n]
    
    # Format the results
    results = []
    for product, similarity in top_similar:
        results.append({
            'name': product['name'],
            'type': product['type'],
            'price': product['price'],
            'store_name': product['store_name'],
            "description":product['description'],
            'score': similarity
        })
    
    return results

def find_top_k(selected_product, num_products):
    """
    Find the top K similar products excluding the selected product itself.
    
    :param selected_product: Name of the selected product
    :param num_products: Number of similar products to retrieve
    :return: Prints the top K similar products
    """
    query = {"name": {"$eq": selected_product}}
    result = products_collection.find_one(query)

    if result and 'embedding' in result:
        similar_products = vector_search(result["embedding"], selected_product, num_products)
        return similar_products
    else:
        print(f"Product '{selected_product}' not found or has no embedding.")
