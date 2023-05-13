s1={11,11,22,33,44,50,55}
## s1[0]=11 we can not fatch any value
# print(s1)
# s1.add(99)
# # s1.sort() we can not sort set
# print(s1)
# # del s1(22) can not delete function cell
# s1.remove(22)
# #s1.remove(22)
# print(s1)
# s1.discard(11)
# # s1.discard(11)  it will not throw any error
# print(s1)

s2={90,70,50,40,50,30,20,60}
# print(60 in s2)
print(s2)

print(s1.union(s2))

print(s1.intersection(s2)) #common value will print

s1.update(s2)
print(s1)
print(s2)
s2.update(s1)
print(s2)