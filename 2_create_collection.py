import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']

# #creating a collection called 'customers'
# mycollection = mydb['customers']

# #check if a collection item exist
# print(mydb.list_collection_names())

collectionlist = mydb.list_collection_names()
if "customers" in collectionlist:
  print("The collection exists.")