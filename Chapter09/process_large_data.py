import csv
import pymongo
from pymongo import MongoClient

## create a MongoClient object,
## used to connect and interface
## with mongodb
client = MongoClient()

## these two lines create a collection
## object which allows you to interface
## with a particular collection
db = client.weather
collection = db["records2"]

## read data line by line and
## insert each row as a document
## into the database collection
fin = open("data/fake_weather_data.csv","r",newline="")
reader = csv.DictReader(fin)
for row in reader:
    collection.insert_one(row)

fin.close()
