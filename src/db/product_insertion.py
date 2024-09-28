from pymongo import ASCENDING
from pymongo.errors import ServerSelectionTimeoutError, WriteError
import json
import numpy as np
from scipy.spatial.distance import cosine
from src.db.db_connection import client,db,products_collection,COLLECTION_NAME

def init_db():
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB")
        
        if COLLECTION_NAME not in db.list_collection_names():
            db.create_collection(COLLECTION_NAME)
            print(f"Collection '{COLLECTION_NAME}' created.")
        
        # Create an index on the embedding field for faster similarity searches
        products_collection.create_index([("embedding", ASCENDING)])
        print("Created index on embedding field.")
        
        return True
    except ServerSelectionTimeoutError:
        print("Unable to connect to the MongoDB server. Please check if it's running and the connection string is correct.")
        return False

def add_product(name, type, price, quantity, description, store_name, embedding_vector):
    
    product = {
        "name": name,
        "type": type,
        "price": price,
        "quantity": quantity,
        "description": description,
        "store_name": store_name,
        "embedding": embedding_vector
    }
    try:
        result = products_collection.insert_one(product)
        print(f"Added product: {name} with id: {result.inserted_id}")
    except WriteError as e:
        print(f"Error adding product {name}: {e}")

def load_products_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            products_data = json.load(file)
        
        for product in products_data:
            embedding = product['embedding']
            if isinstance(embedding, str):
                embedding = [float(x) for x in embedding.strip('[]').split(',')]
            
            
            add_product(
                name=product['name'],
                type=product['type'],
                price=product['price'],
                quantity=product['quantity'],
                description=product['description'],
                store_name=product['store_name'],
                embedding_vector=embedding
            )
        
        print(f"Loaded {len(products_data)} products from JSON")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")

def vector_search(query_embedding, n=5):
    """
    Perform a vector similarity search using cosine similarity.
    
    :param query_embedding: The query vector (must be 382-dimensional)
    :param n: Number of similar products to return
    :return: List of similar products
    """
   
    query_embedding = np.array(query_embedding)
    
    # Fetch all products from the database
    all_products = list(products_collection.find({}, {'name': 1, 'type': 1, 'price': 1, 'store_name': 1, 'embedding': 1}))
    
    # Calculate cosine similarity for each product
    similarities = []
    for product in all_products:
        product_embedding = np.array(product['embedding'])
        similarity = 1 - cosine(query_embedding, product_embedding)  # Convert distance to similarity
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
            'score': similarity
        })
    
    return results

if __name__ == "__main__":
    if init_db():
        # Load products from JSON file if not already loaded
        #load_products_from_json('../data/fake_clothing_products.json')
        
        # Read the first entry from the JSON file
        with open("../data/fake_clothing_products.json", "r") as file:
            products_data = json.load(file)
            if products_data:
                first_product = products_data[0]
                query_embedding = first_product['embedding']
                
                # Ensure the embedding is a list of floats
                if isinstance(query_embedding, str):
                    query_embedding = [float(x) for x in query_embedding.strip('[]').split(',')]
                
                print(f"Using embedding from product: {first_product['name']}")
                
                # Perform vector search
                try:
                    similar_products = vector_search(query_embedding)
                    print("\nSimilar products:")
                    for product in similar_products:
                        print(f"{product['name']} (Score: {product['score']:.4f})")
                except Exception as e:
                    print(f"Error during vector search: {e}")
            else:
                print("No products found in the JSON file.")
    else:
        print("Database initialization failed. Please resolve the issues and try again.")