from pymongo import MongoClient

DATABASE_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "myDatabase"
COLLECTION_NAME = "products"

client = MongoClient(DATABASE_URL)
db = client[DATABASE_NAME]
products_collection = db[COLLECTION_NAME]
