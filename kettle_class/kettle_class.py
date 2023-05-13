class Kettle:
    def __init__(self,name,model,price,status):
        self.name=name
        self.model=model
        self.price=price
        self.status=status

    def show_details(self):
        print("kettle name: {} kettle model: {} kettle price: {}".format(self.name,self.model,self.price))

    def switchon(self):
        self.status=True
    def switchoff(self):
        self.status=False

k1=Kettle("Philips","p001","1001",False)
# k1.show_details()
print(k1.status)
k1.switchon()
print(k1.status)
k1.switchoff()
print(k1.status)

k2=Kettle("Bosch","p002","1005",False)
# k2.show_details()
k3=Kettle("LG","p003","1007",False)
k4=Kettle("MI","p004","1009",False)

allkettels=[k1,k2,k3,k4]
for i in allkettels:
    i.show_details()
    if(i.status==False):
        i.switchon()
        print(i.status)
        i.switchoff()
        print(i.status)