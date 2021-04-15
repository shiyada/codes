import pymongo
import csv
import json
import sys, getopt, pprint
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydb']
mycol = mydb["births"]
csvfile=open("births.csv",'r')
reader = csv.DictReader( csvfile )
header= ["year","month","day","gender","births"]
x=mycol.drop()
count=0
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    # print(row)
    count=count+1
    mycol.insert(row)
# mydict = { "name": "nuthan", "address": "andra" }
# x = mycol.insert_one(mydict)


print(count)