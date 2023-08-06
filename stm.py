#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      USER
#
# Created:     17-08-2019
# Copyright:   (c) USER 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import platform
from pymongo import MongoClient  # import mongo client to connect
import pprint
import datetime
import hashlib

sqlstr="select ecode,ename,phone,DOB from employee where salary>1000 and salary<5000"
     # Convert the query in lower case

#sqlstr=str(input("Enter the SQL Query Statement:"))
sqlstr=sqlstr.lower()

# Relational and Logical Operator
dictrelational={"=":"$eq","<>":"$ne",">":"$gt",">=":"$gte","<":"$lt","<=":"$lte"}
dictlogical={"not":"$not","and":"$and","or":"$or"}

totlist=sqlstr.partition("where") # Break the string 1+where+2
margetoken=totlist[0]             # margetoken contain 1 before where part

token1=sqlstr.partition("from")
token2=token1[0]
token3=token2.partition("select")
token4=token3[2]
token4=token4.strip()  # remove all blanks lstrip(), rstrip()
pitoken=token4.split(",")

token5=totlist[2] # rest of the where part of the query
condlist=[]
opcondlist=[]


print()
print("Token 4 for Projection:",token4)  # REMOVE it

margetoken=sqlstr.split()  # Split the query in space wise & store  in to a list
mql=""

l=len(margetoken)
print("Lenth:",l)   # REMOVE it
i=margetoken.index("from")
mql="db."+ margetoken[i+1]
#---------------------------------------------------------------
if pitoken[0]=="*" and "where" not in totlist[1]:
 if margetoken[0]=="select":
   mql=mql +"."+"find("
   if  margetoken[1]=="*":
    mql=mql + ")"
    print(mql)
#---------------------------------------------------------------
elif "*" not in pitoken[0] and "where" not in totlist[1]:
 if margetoken[0]=="select":
   mql=mql +"."+"find({},{"
   lp=len(pitoken)
   c=1
   print("LENGTH PI:",lp)      # REMOVE it
   for x in pitoken:
    if c<lp:
     mql=mql + '"' + x + '"' + ": 1,"
     c=c+1
    else:
     mql=mql + '"' + x + '"' + ": 1})"
   print(mql)

#---------------------------------------------------------------
if pitoken[0]=="*" and "where" not in totlist[1]:
 if margetoken[0]=="select":
   mql=mql +"."+"find("
   if  margetoken[1]=="*":
    mql=mql + ")"
    print(mql)
#---------------------------------------------------------------
 else:
    print()
#---------------------------------------------------------------
 print()
print("Index of from is:",i)      # REMOVE it
for x in token5:
 if (x>="a" and x<="z") or (x>=0 and x<=9):
   condlist.append(x)

  print(x);

print()






