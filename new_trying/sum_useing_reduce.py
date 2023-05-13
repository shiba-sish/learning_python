from functools import  reduce
l1=[10,20,30,40,50]
def tsum(a,b):
    return a+b
print(reduce(tsum,l1,0))