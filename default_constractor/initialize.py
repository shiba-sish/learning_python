class Student:
    def __init__(self,name,address,course,fee):
        self.name=name
        self.address=address
        self.course=course
        self.fee=fee
        print("student {}  stored successfuly".format(self.name))

    def fees(self):
        self.fee=False

    def paidfees(self):
        self.fee= True

s1=Student("raju","dholakpur","engg",False)
s2=Student("bhim","dholakpur","mba",True)

l1=[s1,s2]
for i in l1:
    if(i.fee==False):
        print("pay the fees immediately")
        i.fees()
    else:
        print("fees already paid")
        i.paidfees()



print(s1.name +" "+ s1.address +" "+ s1.course)
print(s2.name +" "+ s2.address +" "+ s2.course)

print(s1)
print(s2)

#renaming update variables
s1.name="chutki"
s2.name="kalia"

print(s1.name +" "+ s1.address +" "+ s1.course)
print(s2.name +" "+ s2.address +" "+ s2.course)

#inbuild function
print(hasattr(s1,"name")) #true or false
print(getattr(s1,"name")) # get the value
print(hasattr(s1,"phone")) #true or false
print(setattr(s1,"phone",912345678)) # set the attribute value # none
print(hasattr(s1,"phone")) #true or false
print(delattr(s1,"phone")) #none
print(hasattr(s1,"phone")) #true or false