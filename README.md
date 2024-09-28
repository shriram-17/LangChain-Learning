
# Product Embeddings Search Application

## Overview
The Product Embeddings Search Application is designed to store product data and descriptions in a local MongoDB database. It allows users to query products, calculate cosine similarity, and interact with a user-friendly interface built using HTML. The application leverages the ILLAMA model for product description generation and the Sentence Transformer for text generation to enhance the search capabilities.

## Features
- **Product Storage**: Store product data and descriptions in a local MongoDB database.
- **Product Description Generation**: Utilize the ILLAMA model for generating detailed product descriptions.
- **Text Embedding Generation**: Use Sentence Transformer to create embeddings for the product descriptions.
- **Querying Mechanism**: Retrieve products based on user input.
- **Cosine Similarity Calculation**: Find the top K similar products based on user queries.
- **User-Friendly Interface**: A simple HTML-based application for user interactions.

## Getting Started

### Prerequisites
- Python 3.x
- Local MongoDB instance
- Flask
- Required Python libraries (e.g., LangChain, Sentence Transformer, PyMongo)

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd product-embeddings-search
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB**:
   - Ensure you have a local MongoDB instance running.
   - Create a database and a collection to store products and descriptions.

4. **Configure Environment Variables**:
   - Create a `.env` file in the root directory and add your MongoDB connection details.

5. **Run the Flask Application**:
   ```bash
   flask run
   ```

## Remaining Tasks
1. **Storing Products in MongoDB**
   - Implement functionality to store product data and descriptions in the local MongoDB database.

2. **Generating Product Descriptions**
   - Utilize the ILLAMA model to generate detailed product descriptions.

3. **Generating Text Embeddings**
   - Use Sentence Transformer to create embeddings for the product descriptions.

4. **Querying Products**
   - Develop a querying mechanism to retrieve products based on user input.
   - Create an API endpoint in Flask that accepts user queries and implements logic to fetch relevant products from the database.

5. **Finding Cosine Similarity with Top K Results**
   - Implement cosine similarity calculation to find the top K similar products based on their embeddings.
   - Use NumPy or another library to compute cosine similarity between the query embedding and stored embeddings, returning the top K results based on similarity scores.

6. **Integrating with Basic Flask App**
   - Finalize the integration of the backend with the Flask application.
   - Set up routes for displaying HTML pages and handling form submissions, ensuring smooth interaction between frontend and backend components.

7. **User Interaction with HTML Pages**
   - Create user-friendly HTML pages for interaction.
   - Design a search page where users can input queries and display results in an organized manner, showing product names and similarity scores.

## Next Steps
- Prioritize tasks based on dependencies (e.g., storing data should be completed before querying).
- Assign deadlines for each task to ensure timely completion.
- Test each component thoroughly after implementation to ensure functionality.

## Conclusion
Completing these tasks will result in a fully functional Product Embeddings Search Application that allows users to efficiently search for similar products based on their embeddings.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
