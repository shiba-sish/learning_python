# s1=input("enter the string")
# d1={}
# for letter in s1:
#     if letter not in d1:
#         d1[letter]=1
#     else:
#         d1[letter]=d1[letter]+1
# print(d1)

# # each word in a string
# s1=input("enter the string")
# d1={}
# s2=s1.split(" ")
# s3="_".join()
# for i in s1:
#     if letter not in d1:
#         d1[letter]=1
#     else:
#         d1[letter]=d1[letter]+1
# print(d1)

# print([i for i  in range (1,11)])

# print([i*i for i  in range (1,11)])

# print([i for i in range (1,101) if i%3==0])

# l1=[5,6,3,7,8,34,65]
# print({i for i in l1 if i%2==0})

#d1={1:"ram",2:"sam",3:"rajesh",4:"shiba",5:"kantara",6:"joti"}
d1={}
l1=["ram","sam","shiba","kesav","nagesh","joti","rohit","roshan"]
# for i in range(0,len(l1)):
#     d1[i+1]=l1[i]
# print(d1)

# print({i+1:l1[i] for i in range (0,len(l1))})
print({i:i**2 for i in range (1,11)})
print({i:i**3 for i in range (1,11)})
print({i:i**3 for i in range (1,11) if i%2==0})