# SQL to MQL conversion of code  PYTHON AND MONGODB

import os
import platform
from pymongo import MongoClient # import mongo client to connect
import pprint
import datetime
import hashlib
# Creating instance of mongoclient
global count
client = MongoClient()
# Creating database or switch to an existing database [client.name_of_the_database]
db = client.adi

		# COUNT LAST DUCUMENT OR Blockno
global examyear

def manageExamBlockChain():
     print("""
Enter 1 : INSERT command
Enter 2 : UPDATE Command
Enter 3 : SELECT Command
Enter 4 : DELETE Command

		""")
     #count1=db.employees.count()

     try: #Using Exceptions For Validation
	  	  userInput = int(input("Please Select An Above Option( 1-4): ")) #Will Take Input From User
     except ValueError:
       exit("\nHy! That's Invalid Input , Enter (1-4)") #Error Message
     else:
	      print("\n") #Print New Line


     if(userInput == 1): #This Option Will Print List Of Data
    	  
         
     elif(userInput == 2): #This Option Will Add New Student In The List
           #*****************************************************************************************************
              # FETCH LAST HASH VALUE
       if count1>0:
            phash=db.employees.find({"Blockno":count1},{"Hashvalue":1})
            for ph in phash:
                pvh=ph['Hashvalue']

              #********************************************************************************************************
##            if count == 0:
##                   employee = {"Blockno":1,"previoushash": 0,
##                     "name": "GENESIS BLOCK",
##                      "Alldata":"Data Available from Next Block of Chain","Hashvalue":calhash()
##                     }

            examname = input("Enter Exam Name: ")
            examyear = input("Enter Exam Year: ")
            examsem = input("Enter Semester of Exam: ")
            examstart = input("Enter Starting Date of Exam: ")
            examend = input("Enter Concluding Date of Exam: ")
            bos = input("Enter Board of Studies of Exam: ")
            examfy = input("Enter Whether Final Semester of Exam(y or n) : ")

                #------------------------------------------------------------------------
                # HAsh VALUE CALCULATION
            header_bin = (str(examyear) + str(examname)+ str(examsem)+ str(examstart)+ str(examend) + str(bos)+ str(datetime.datetime.now()))
            inner_hash = hashlib.sha256(header_bin.encode()).hexdigest().encode()
            outer_hash = hashlib.sha256(inner_hash).hexdigest()
                #------------------------------------------------------------------------

            employee = {"Blockno":count1+1,
                         "previoushash":pvh,
                         "Examination":examname,
                         "BOS":bos,
                         "ExamYear":examyear,
                         "Semester":examsem,
                         "CommencingDate":examstart,
                         "ConclusionDate":examend,
                         "Finalsem":examfy,
                         "Timestamp":datetime.datetime.now(),
                         "Hashvalue": outer_hash

                          }
                # Creating document
            employees = db.employees
                 # Inserting data
            employees.insert_one(employee)
                   # Fetching data
            #count=count+1
            print("Inserted Succesfully")

 # HAsh VALUE CALCULATION


manageExamBlockChain()

def runAgain(): #Making Runable Problem1353
	runAgn = input("\nwant To Run Again Y/n: ")
	if(runAgn.lower() == 'y'):

		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls'))
		else:
			print(os.system('clear'))

		manageExamBlockChain()
		runAgain()
	else:

         quit() #Print GoodBye Message And Exit The Program

runAgain()
  #pprint.pprint(employees.find_one())