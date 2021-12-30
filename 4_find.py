import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

# #Return only the names and addresses, not the _ids:
# for x in mycollection.find({},{"_id":0, "name": 1, "address": 1 }):
#     print(x)

#=================================

#This example will exclude "address" from the result
for x in mycollection.find({},{'address':0}):
    print(x)

