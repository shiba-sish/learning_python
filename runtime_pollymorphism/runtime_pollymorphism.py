class Manufractuer:
    def selllaptop(self):
        print("we manufracture all laptop");
class Dell(Manufractuer):
    def selllaptop(self):
        print("we manufracture Dell laptop")
class HP(Manufractuer):
    def selllaptop(self):
        print("we manufracture HP laptop")
class Lenovo(Manufractuer):
    def selllaptop(self):
        print("we manufracture Lenovo laptop")
class Asus(Manufractuer):
    def selllaptop(self):
        print("we manufracture Asus laptop")

class Flipkart:
    def selleverything(self,m):
        m.selllaptop()


d1=Dell()
# d1.selllaptop()
d2=HP()
# d2.selllaptop()
d3=Lenovo()
# d3.selllaptop()
d4=Asus()
# d4.selllaptop()
f=Flipkart()
f.selleverything(d1)
f.selleverything(d2)
f.selleverything(d3)
f.selleverything(d4)