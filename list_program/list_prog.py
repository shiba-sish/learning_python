# s1=[10,2.33,'asc',"safga"]
# print(s1)
# s1=[11,22,33,44,55,555]
# print(s1[0])
# print(s1[-2])
# print(s1[:])
# print(s1[0:])
# print(s1[:len(s1)])
# print(s1[0:len(s1)])
# print(s1[: :])
# print(s1[: :2])
# print(s1[: :4])
# print(s1[: :-1])
# print(s1[: :-2])
# print(s1[4:7])
# print(s1[4:7])
# print(55 in s1)
# print(55 not in s1)
# print(dir(list))
# s1[0]=1000
# print(s1)
# # s1.clear()
# s2=[] # empty list
# s2=[1000] # empty list
# print(s2)
# s3=list()# empty list
# s2=s1.copy()
# print(s2)

# s1=[11,22,33,44,55,555]
# print(s1)
# s1.append(222)# add last index
# print(s1)
# s1.pop()# remove last index
# print(s1)
# s1.remove(55)
# print(s1)
#
# # s1.insert(2,"hi")# add in between any list(it will no delete any thing only shift to next index)
# # print(s1)
#
# s1.reverse()
# print(s1)
#
# s1.sort()
# print(s1)

e1=list()
for i in range(1,11):
    e1.append(2*i)
print(e1)

e1=[]
for i in range(1,11):
    e1.append(2*i-1)
print(e1)

squre=[]
for i in range (1,11):
    squre.append(i**2)
print(squre)

s1=[11,22,33,44,55,555]
print(max(s1))
print(min(s1))