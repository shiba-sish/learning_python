'''
Created on 21-Mar-2023

@author: Shibasish China
'''
a=int(input("first value "))
b=int(input("second value "))
c=int(input("third value "))

if(a>b and a>c):
    print(str(a)+" gretest no")
elif(b>c):
    print(str(b)+f" gretest no") # here f refer to previous formate
else:
    print(str(c)+f" gretest no")