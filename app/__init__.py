from flask import Flask
from pymongo import MongoClient
from app.config.config import Config

app = Flask(__name__)
mongo_client = MongoClient(host=Config.MONGODB_HOST, port=27017)
db = mongo_client[Config.MONGODB_DATABSE]


from app.controllers import DefaultController
from app.controllers import GitController