i=1
while i<=10:
    print(2**i)
    i+=1

#global and local variables
a=10
def add3():
    a=10
    b=30
    print(a+b)
add3()
    
