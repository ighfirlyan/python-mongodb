import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

#In MongoDB, a database is not created until it gets content!

# #create database called 'mydatabase'
# mydb = myclient['mydatabase']

#=======================================

# #check if database exists
# print(myclient.list_database_names())

#========================================

#or
dblist = myclient.list_database_names()

if 'mydatabase' in dblist:
    print('the database exists')