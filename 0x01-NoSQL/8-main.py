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
insert_school = __import__('9-insert_school').insert_school
update_topics = __import__('10-update_topics').update_topics

if __name__ == "__main__":
    client = MongoClient(url)
    school_collection = client.test_db.school
    new_school_id = insert_school(
        school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('address', "")))

    update_topics(school_collection, "Holberton school",
                  ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('topics', "")))
