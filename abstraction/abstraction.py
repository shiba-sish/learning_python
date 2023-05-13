from abc import ABC,abstractmethod
class Car:
    def milage(self):
        pass
class Maruti(Car):
    def milage(self):
        print("25km/lit")
class Audi(Car):
    def milage(self):
        print("10km/lit")
m1=Maruti()
m1.milage()
m2=Audi()
m2.milage()