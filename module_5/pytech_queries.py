import pymongo
from pymongo import MongoClient

# display all documents in the collection
docs = pytech.find()

for doc in docs:
    print(doc)
    
# display a single document by student_id
print(pytech.find_one({"student_id": "1008"}))