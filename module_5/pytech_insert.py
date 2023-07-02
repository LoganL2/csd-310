import pymongo
from pymongo import MongoClient

# Create a pymongo client
client = MongoClient("localhost", 27017)

# Get the database instance
db = client["mydb"]

# db collection
pytech = db["PyTech"]

# insert 3 students
records = [
    {
        "student_id": "1007",
        "first_name": "George",
        "last_name": "Washington"
    },
    {
        "student_id": "1008",
        "first_name": "Logan",
        "last_name": "Lilley"
    },
    {
        "student_id": "1009",
        "first_name": "Seth",
        "last_name": "Brown"
    }
]

for record in records:
    new_student_Id = pytech.insert_one(record).inserted_id
    print(new_student_Id)