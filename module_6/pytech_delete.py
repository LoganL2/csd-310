import pymongo
from pymongo import MongoClient

conn = MongoClient()
db = conn.pytech
students = db.students

records = [
    {
        "student_id": "1010",
        "first_name": "Dead",
        "last_name": "Fred"
    }
]

for record in records:
    new_student_Id = students.insert_one(record).inserted_id
    print(new_student_Id)

for record in records:
    find = students.find(students)
    print(find)

for record in records:
    find_one = students.find_one(
        {
        "student_id" : "1010"}
    )
    print(find_one)

for record in records:
    delete_one = students.delete_one(
        {
        "student_id" : "1010"}
    )
    print(delete_one)

for record in records:
    find = students.find(students)
    print(find)