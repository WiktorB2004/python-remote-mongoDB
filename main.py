# Imports
from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
# Config
load_dotenv(find_dotenv())

# Env variables
password = os.environ.get('MONGODB_PWD')

# MongoDB connection configuration
connection_string=f'mongodb+srv://WiktorB2004:{password}@python-remote-control.ae16b9l.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(connection_string)
dbs = client.list_database_names()
