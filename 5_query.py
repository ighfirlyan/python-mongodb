import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

# #Filter the result
# myquery = { 'address': 'Park Lane 38'}

# mydoc = mycollection.find(myquery)

# for x in mydoc:
#     print(x)

#========================

# #Find documents where the address starts with the letter "S" or higher
# myquery = {'address': {'$gt': 'S'}}

# mydoc = mycollection.find(myquery)

# for x in mydoc:
#     print(x)

#To find only the documents where the "address" field starts with the letter "S", 
#use the regular expression {"$regex": "^S"}

myquery = {'address': {'$regex': '^S'}}

mydoc = mycollection.find(myquery)

for x in mydoc:
    print(x)
