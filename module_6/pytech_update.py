import pymongo
from pymongo import MongoClient

conn = MongoClient()
db = conn.pytech
students = db.students
cursor = students.find()
for record in cursor:
    print(record)

result = students.update_one(
    {"student_id":1007},

        {
        "$set":{
            "last_name":"Joe"
            }
        }
)

cursor = students.find()
for record in cursor:
    print(record)