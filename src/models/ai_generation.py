import logging
import json
import os
from dotenv import load_dotenv
from src.models.groq_api import GroqAPIWrapper
from sentence_transformers import SentenceTransformer
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv("groq_token")
if not api_key:
    raise ValueError("Token not found in environment variables")
else:
    logger.info("API key loaded successfully.")


def generate_product_descriptions(products):
    # Initialize the Groq API wrapper
    groq_api = GroqAPIWrapper(api_key)

    # Create a prompt template for the product description
    template = (
        "Generate a brief product description (2-3 lines) for {name} sold at a store named '{store_name}'. "
        "These {type} are stylish and comfortable, perfect for casual outings or workouts. "
        "They are priced at ${price} with {quantity} in stock. Highlight their versatility and comfort."
    )
    
    # Create a PromptTemplate instance
    prompt_template = PromptTemplate(template=template, input_variables=["name", "store_name", "type", "price", "quantity"])

    # Generate descriptions for each product
    for product in products:  # Limit to first 2 products for testing
        logger.info(f"Generating description for product: {product['name']}")
        try:
            # Create the full prompt using the template and product details
            prompt = prompt_template.format(
                name=product["name"],
                store_name=product["store_name"],
                type=product["type"],
                price=product["price"],
                quantity=product["quantity"]
            )
            
            response = groq_api.query(prompt)
            
            product["description"] = response.strip() 
            logger.info(f"Description generated for {product['name']}: {response}")
        except Exception as e:
            logger.error(f"Error generating description for {product['name']}: {str(e)}")

def compute_embeddings(products):
    model = SentenceTransformer('all-MiniLM-L6-v2')  
    for product in products:
        description = product.get("description")
        if description:
            product["embedding"] = model.encode(description).tolist() 
            logger.info(f"Computed embedding for {product['name']}")

def load_products(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_products(file_path, products):
    with open(file_path, 'w') as file:
        json.dump(products, file, indent=4)

if __name__ == "__main__":
    try:
        # Load the products from JSON file
        products = load_products('./src/data/fake_clothing_products.json')

        # Generate product descriptions
        #generate_product_descriptions(products)

        # Compute embeddings for the generated descriptions
        compute_embeddings(products)

        # Save the updated products back to a JSON file
        save_products('./src/data/fake_clothing_products.json', products)

        logger.info("Product descriptions and embeddings generated and saved successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")