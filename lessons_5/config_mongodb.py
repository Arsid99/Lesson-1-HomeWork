from pymongo import MongoClient

host = MongoClient(port=27017)
database = host.Sydorenko_DB
coll = database.Lesson_5