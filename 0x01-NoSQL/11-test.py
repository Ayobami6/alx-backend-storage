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
schools_by_topic = __import__('11-schools_by_topic').schools_by_topic

if __name__ == "__main__":
    client = MongoClient(url)
    school_collection = client.test_db.school
    j_schools = [
        {'name': "Holberton school", 'topics': [
            "Algo", "C", "Python", "React"]},
        {'name': "UCSF", 'topics': ["Algo", "MongoDB"]},
        {'name': "UCLA", 'topics': ["C", "Python"]},
        {'name': "UCSD", 'topics': ["Cassandra"]},
        {'name': "Stanford", 'topics': ["C", "React", "Javascript"]}
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'),
              school.get('name'), school.get('topics', "")))
