# python-flask-mongodb
REST API using python and flask. Data stored in mongodb

# Create a virtual environment and use it
- mkvirtualenv python-flask-mongodb
- workon python-flask-mongodb

# Install the dependencies using pip
- pip3 install -r requirements.txt

# Install MongoDb and start its daemon
- mongod

# Login into the mongo shell and create a database
- mongo
- use python_flask_mongodb

# Run the app
python3 application.py

# Browse the app in
http://127.0.0.1:5000/

# Create single user using curl
```json
curl -XPOST http://localhost:5000/api/v1/user -H "Content-Type: application/json" -d '{
    "name": "Abhinayak Swar",
    "location": "Nepal"
}'
```

# Create multiple user using curl
```json
curl -XPOST http://localhost:5000/api/v1/user -H "Content-Type: application/json" -d '[
    {
        "name": "Atul Pradhan",
        "location": "Nepal"
    },
    {
        "name": "Pramod Sthapit",
        "location": "Nepal"
    }
]'
```

# Get all the users
```json
curl -XGET http://localhost:5000/api/v1/user
```

# Edit user by id
```json
curl -XPUT http://localhost:5000/api/v1/user/{user_id} -H "Content-Type: application/json" -d '{
    "name": "Abhinayak Swar 123",
    "location": "Nepal"
}'
```

# Delete user by id
```json
curl -XDELETE http://localhost:5000/api/v1/user/{user_id}
```