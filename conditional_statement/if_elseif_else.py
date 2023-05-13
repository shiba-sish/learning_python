'''
Created on 21-Mar-2023

@author: Shibasish China
'''

# a=int(input("first value "))
# b=int(input("second value "))
#
# if(a<b):
#     print(str(a)+"less then"+str(b))
# else:
#     print(str(a)+"greater then"+str(b))

username= input("enter the username :")
#
# if(username=="shiba"):
#     password= int(input("enter the password"))
#     if(password==int("123")):  #string converted to integer
#         print("access granted to-"+username)
#     else:
#         print("access denied password not matched")
# else:
#     print("access denied user name not matched")

if username=="shiba":
    print("access granted "+username)
elif username=="ram":
    print("access granted "+username)
elif username=="sam":
    print("access granted "+username)
else:
    print("access denied for "+username)
    