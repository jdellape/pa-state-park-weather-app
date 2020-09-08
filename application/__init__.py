from flask import Flask
from config import Config
from mongoengine import connect
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

client = MongoClient(Config.DB_URI)
db = client.get_database('PaStateParksDB')

from application import routes