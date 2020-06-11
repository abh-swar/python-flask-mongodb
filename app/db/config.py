from pymongo import MongoClient

DATABASE = MongoClient()['python_flask_mongodb']
DEBUG = True
client = MongoClient('localhost', 27017)