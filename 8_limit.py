import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
mycollection = mydb['customers']

#Limit the result to only return 5 documents
myresult = mycollection.find().limit(5)

for x in myresult:
    print(x)