import os
import sys
import time
import shutil

#---Declare Global Variables-----
time_string=time.localtime()
TS=time.strftime("_%m_%d_%Y_%M_%S",time_string)

def COPY_FILE():

  print("Hi, I am here to help you copy of file or directory")
  time_string=time.localtime()
  TS=time.strftime("%m_%d_%Y_%M_%S",time_string)
  print("The formatted time is {}".format(TS))
 #####FUNCTION DEFINITION#####

def BACKUP_DATABASE():

  print("Hi, I am here to help you backup a database schema")

 #####FUNCTION DEFINITION#######

def CLOUD_MIGRATION():

  print("Hi, I am here to help you migrate data into the AWS cloud")


if __name__=="__main__":

 #####PROGRAM BODY AND FUNCTION CALLS######

  user_in=(raw_input("""What do you want to do?\nEnter C to copy a file or directory\nEnter D to backup a database\nEnter M to migrate data into the AWS cloud\nEnter Input: """)).upper()

if user_in=='C':
   COPY_FILE()
   src=raw_input("Please enter source file or Directory path: ")
   dst=raw_input("Please enter the destination path: ")

   shutil.copytree(src, dst + TS)
   print("Successfully copied to the backup location ")

elif user_in=='D':
   BACKUP_DATABASE()

elif user_in=='M':
   CLOUD_MIGRATION()

else:
   print("You entered the wrong input")
