s1="shibasish"
# s=list(s1)
#
# freq=[s.count(i) for i in s]
# print(dict(zip(s,freq)))

d={}
for i in s1:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)