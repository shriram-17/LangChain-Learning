from flask import Flask, render_template, request, redirect, url_for
from src.db.db_connection import products_collection
from src.utils.cos_sim import find_top_k
import os

# Define the template folder inside src
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src/templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def home():
    # Retrieve distinct product names from MongoDB
    distinct_names = products_collection.distinct("name")

    similar_products = None  # Default to None unless the form is submitted

    if request.method == 'POST':
        selected_product = request.form.get('product_name')  # Get the selected product
        num_products = request.form.get('num_products')  # Get the number of similar products
        
        # Validate form inputs
        if selected_product and num_products:
            num_products = int(num_products)  # Convert num_products to an integer
            
            # Find the top K similar products using cosine similarity
            similar_products = find_top_k(selected_product, num_products)
        else:
            return redirect(url_for('home'))  # Redirect if form inputs are invalid

    # Pass distinct names and similar products to the template
    return render_template('index.html', distinct_names=distinct_names, similar_products=similar_products)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

