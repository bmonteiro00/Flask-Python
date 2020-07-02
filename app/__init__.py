from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient()
db = client.get_database("gitbase")
collection = db.get_collection("git")

from app.controllers import DefaultController
from app.controllers import GitController