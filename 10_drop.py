import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

#You can delete a table, or collection as it is called in MongoDB, by using the drop() method
mycollection.drop()