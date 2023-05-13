class Account:
    def __init__(self,name,address,balence):
        self.name=name
        self.address=address
        self.balence=balence
        print("account created successfully for {}".format(self.name))
    def showbalence(self):
        print("Acoount holder: {} have balence: {}".format(self.name,self.balence))
    def depositmoney(self,amount):
        if amount > 0:
            self.balence=self.balence+amount
            print("Acoount holder: {} have new balence: {}".format(self.name,self.balence))
        else:
            print("ammount should be gretter the 0")
    def withdrow(self,amount):
        if amount<=self.balence:
            self.balence=self.balence-amount
            print("Acoount holder: {} have new balence: {}".format(self.name, self.balence))
        else:
            print("insufficent balance")

p1=Account("Raj","bengluru",5000)
p1.showbalence()
p1.depositmoney(5000)
p1.withdrow(2000)
p1.withdrow(12000)

#single level inheritance
#multi level inheritance
#hybrid inheritance
class Canada(Account):
    def showbalence(self):
        print("Acoount holder: {} address: {} have balence: {}".format(self.name, self.address, self.balence))
# class HDFC (Canada):
#     pass
# #hirechitical inheritance
# class HDFC (Account):
#     pass
# #multiple inheritance is possible in python through class
# class UCO (Account,Canada,HDFC):
#     pass

p4=Canada("suresh", "bangalore" , 10000)
p4.showbalence()
p4.depositmoney(30000)
p4.withdrow(5000)




