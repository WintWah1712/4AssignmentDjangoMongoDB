import pymongo
connection = pymongo.MongoClient('localhost',27017)
database = connection['miniDB']
collection = database['miniUserCollection']
