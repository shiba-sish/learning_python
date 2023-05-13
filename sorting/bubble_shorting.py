l1=[2,4,5,8,3,2,5,9,11,99,1]
for j in range(1, len(l1)):
    for i in range(0,len(l1)-j):
        if l1[i]>l1[i+1]:
            temp=l1[i]
            l1[i]=l1[i+1]
            l1[i+1]=temp

print(l1)