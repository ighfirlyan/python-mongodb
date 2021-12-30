import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

myquery = {"address": "Mountain 21" }

# #delete 1 document with address 'Mountain 21'
# x = mycollection.delete_one(myquery)

# print(x.deleted_count, " documents deleted.")

#====================================

# #Delete all documents were the address starts with the letter S
# myquery = {'address': {'$regex': '^S'}}

# x = mycollection.delete_many(myquery)

# print(x.deleted_count, " documents deleted.")

#====================================

x = mycollection.delete_many({})

print(x.deleted_count, ' documents deleted.')