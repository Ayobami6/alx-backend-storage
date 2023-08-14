#!/usr/bin/env python3
""" 8-main """
from pymongo import MongoClient

MONGO_USERNAME = 'ayo'
MONGO_PASSWORD = 'haywon'
MONGO_HOSTNAME = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_DB = 'test_db'

url = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}/{MONGO_DB}?authSource=admin'


list_all = __import__('8-all').list_all

if __name__ == "__main__":
    client = MongoClient(url)
    school_collection = client.test_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
