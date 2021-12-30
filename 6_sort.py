import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

# #Sort the result alphabetically by name
# mydoc = mycollection.find().sort('name')

# for x in mydoc:
#     print(x)

#======================================

#sort("name", 1) #ascending
#sort("name", -1) #descending

#Sort the result reverse alphabetically by name
mydoc = mycollection.find().sort('name',-1)

for x in mydoc:
    print(x)