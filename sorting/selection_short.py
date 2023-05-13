l1=[1,2,3,9,8,7,6,5,-4,-2,-3]
def min(l,i):
    minval=l[i]
    minindex=i
    for i in range (0,len(l)):
        if  minval>l[i]:
            minval=l[i]
            minindex=i

    return minindex

def max(l, i):
    maxval = l[i]
    maxindex = i
    for i in range(0, len(l)):
        if maxval > l[i]:
            maxval = l[i]
            maxindex = i

    return maxindex

for i in range (0,len(l1)):
    minindex=min(l1,i)
    t=l1[i]
    l1[i]=l1[minindex]
    l1[minindex]=t
print(l1)