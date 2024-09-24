import json
import random
from typing import List, Dict

class ClothingProductGenerator:
    def __init__(self, num_products: int):
        self.num_products = num_products
        # Predefined list of clothing names and types
        self.clothing_items = [
            {"name": "Casual Jacket", "type": "Jacket"},
            {"name": "Formal Shirt", "type": "Shirt"},
            {"name": "Graphic T-Shirt", "type": "T-Shirt"},
            {"name": "Slim Fit Jeans", "type": "Jeans"},
            {"name": "Chino Pants", "type": "Pants"},
            {"name": "Hooded Sweatshirt", "type": "Hoodie"},
            {"name": "Knitted Sweater", "type": "Sweater"},
            {"name": "Summer Dress", "type": "Dress"},
            {"name": "Athletic Joggers", "type": "Joggers"},
            {"name": "Denim Jacket", "type": "Jacket"},
            {"name": "Checked Shirt", "type": "Shirt"},
            {"name": "Plain T-Shirt", "type": "T-Shirt"},
            {"name": "Bootcut Jeans", "type": "Jeans"},
            {"name": "Cargo Pants", "type": "Pants"},
            {"name": "Zip-Up Hoodie", "type": "Hoodie"},
            {"name": "Wool Sweater", "type": "Sweater"},
            {"name": "Maxi Dress", "type": "Dress"},
            {"name": "Track Pants", "type": "Joggers"},
            {"name": "Leather Jacket", "type": "Jacket"},
            {"name": "Polo Shirt", "type": "Shirt"},
            {"name": "V-Neck T-Shirt", "type": "T-Shirt"},
            {"name": "Skinny Jeans", "type": "Jeans"},
            {"name": "Linen Pants", "type": "Pants"},
            {"name": "Pullover Hoodie", "type": "Hoodie"},
            {"name": "Cardigan Sweater", "type": "Sweater"},
            {"name": "Cocktail Dress", "type": "Dress"},
            {"name": "Fleece Joggers", "type": "Joggers"},
            {"name": "Windbreaker Jacket", "type": "Jacket"},
            {"name": "Flannel Shirt", "type": "Shirt"},
            {"name": "Ringer T-Shirt", "type": "T-Shirt"},
            {"name": "Distressed Jeans", "type": "Jeans"},
            {"name": "Sweatpants", "type": "Pants"},
            {"name": "Cropped Hoodie", "type": "Hoodie"},
            {"name": "Cashmere Sweater", "type": "Sweater"},
            {"name": "A-Line Dress", "type": "Dress"},
            {"name": "Yoga Pants", "type": "Joggers"},
            {"name": "Bomber Jacket", "type": "Jacket"},
            {"name": "Oxford Shirt", "type": "Shirt"},
            {"name": "Tie-Dye T-Shirt", "type": "T-Shirt"},
            {"name": "Mom Jeans", "type": "Jeans"},
            {"name": "Culottes", "type": "Pants"},
            {"name": "Oversized Hoodie", "type": "Hoodie"},
            {"name": "Cable Knit Sweater", "type": "Sweater"},
            {"name": "Midi Dress", "type": "Dress"},
            {"name": "Harem Pants", "type": "Joggers"},
            {"name": "Suede Jacket", "type": "Jacket"},
            {"name": "Chambray Shirt", "type": "Shirt"},
            {"name": "Crop Top", "type": "T-Shirt"},
            {"name": "Wide Leg Jeans", "type": "Jeans"},
            {"name": "Palazzo Pants", "type": "Pants"},
            {"name": "Kangaroo Hoodie", "type": "Hoodie"},
            {"name": "Turtleneck Sweater", "type": "Sweater"},
            {"name": "Wrap Dress", "type": "Dress"},
            {"name": "Jogger Pants", "type": "Joggers"}
        ]
        
    def generate_products(self) -> List[Dict]:
        """Generate a list of clothing products."""
        # Randomly select the required number of products
        selected_products = random.sample(self.clothing_items, min(self.num_products, len(self.clothing_items)))
        
        # Format the products to match our desired output
        formatted_products = []
        for product in selected_products:
            formatted_product = {
                **product,
                # Set additional fields as needed
                'price': round(random.uniform(10.0, 100.0), 2),  # Random price between $10 and $100
                'quantity': random.randint(1, 50), 
                'description': None,
                'embedding': None,
                'store_name': 'Grasp'
            }
            formatted_products.append(formatted_product)
        
        return formatted_products

if __name__ == "__main__":
    num_products = 50
    generator = ClothingProductGenerator(num_products)
    
    try:
        products = generator.generate_products()

        # Save products to a JSON file
        with open('fake_clothing_products.json', 'w') as json_file:
            json.dump(products, json_file, indent=4)

        print(f"{len(products)} fake clothing products saved to 'fake_clothing_products.json'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")