import os
from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()

MONGO_USER = os.environ.get('MONGO_USER')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')
MONGO_DB = os.environ.get('MONGO_DB')
DOMAIN = os.environ.get('DOMAIN')

connect(host=f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{DOMAIN}/{MONGO_DB}?appName=Cluster0", ssl=True)

