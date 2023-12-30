
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://fireplatypus375:0TgN3YyiObPpHtmQ@fblamain.emmytgc.mongodb.net/")
db = cluster["FBLAMain"]
loginInfo = db["login_info"]


