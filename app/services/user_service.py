# Service layer for user
from app.db.config import client
from bson import ObjectId

# Select the database
db = client.python_flask_mongodb
# Select the collection
collection = db.users


def create(body):
    return collection.insert(body)

def update(user_id, body):
    return collection.find_one_and_update(
            {"_id" : ObjectId(user_id)},
            {"$set": body},
            upsert=True)

def get():
    return collection.find()

def count():
    return collection.find().count()

def delete(user_id):
    return collection.delete_one({'_id': ObjectId(user_id)})
