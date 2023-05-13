l1=[11,99,13,14,13,16,17,13,80]

# # using range function
# for i in range (0,len(l1)):
#     print(l1[i])

#without using range funtion(in operator)
# for eachvalue in l1:
#     print(eachvalue)

# #lener search
# count=0
# for i in range(0,len(l1)):
#     if l1[i] == 13:
#         print("13 present")
#         count=count+1
# print(count)
#
# binary search
l1=[11,22,33,44,55,66,77,66,44,22]
b=l1.sort()
print(l1)
for i in range (0,len(l1)):
    if(33<= len(l1)//2):
        if l1[i]==33:
            print("33 present in index "+str(i))
    else:
        if l1[i]==33:
            print("33 present in index "+str(i))

