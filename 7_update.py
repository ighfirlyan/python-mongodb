import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

# #Change the address from "Valley 345" to "Canyon 123"
# myquery = { 'address': 'Valley 345'}
# newvalues = {'$set': {'address':'Canyon 123'}}

# mycollection.update_one(myquery, newvalues)

# for x in mycollection.find():
#   print(x)

#==================================================

#Update all documents where the address starts with the letter "S"

myquery = { 'address':{'$regex':'^S'}}
newvalues = { '$set': {'name': 'Minnie'}}

x = mycollection.update_many(myquery, newvalues)

print(x.modified_count, 'documents updated')