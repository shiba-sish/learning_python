# define a function 


#no parameter function
def add():
    a,b=10,20
    print(a+b)

add()    

#function with parameter
def add1(a,b):
    print(a+b)
add1(10,50)   

# function with return value # returns only one value
def add2(a,b):
    return (a+b)
result=add2(10,40)
print(result)

#global and local variables
a=10
def add3():
    a=10
    b=30
    print(a+b)
add3()

#function with default value
def greetion(username="ram"):
    print("hello "+username)

greetion()
greetion("shiba")

#keyword argument
def hello(lastname="kumar", firstname="ram"):
    print("hello "+firstname+" "+lastname)
hello()
hello("rajesh","sen")
hello(firstname="shiva",lastname="paul")
