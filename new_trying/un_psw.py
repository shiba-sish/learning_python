import re

username=input("enter the user name: ")

if(username.isalnum() == True ):
    print("usename accepted!!!")
    password = input("enter the password: ")
    if(password.isnumeric()== True):
        print("pasword accepted!!!")
    else:
        print("wrong type of password!!!")
else:
    print("wrong type of username!!!")