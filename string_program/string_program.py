# s1="skillmine"
# s2='skillmine'
# s3="welcome to \t 'skillmine'"
# s4='welcome to \n"skillmine"'
# s5='''hello skillmine
# i am \n fine
#
# working fine'''#document string everything will print as it is as doc string
# s6="""hello skillmine
# i am \n fine
#
# working fine"""
# print(s1+" "+s2+" "+s3+" "+s4)
# print(s5)
# print(s6)
# print(type(s1))
# print(type(s2))
#
# ss1="skillmine technology"
#
# a=10
# b=20
# print("sum of {1} and {0} is {2}".format(a,b,(a+b)))
#
# for i in range(1,11):
#     print("{} squre is {} qube is {}".format(i,i*i, i*i*i))
#
# for i in range(10000,999,-1000):
#     print("10% is {} 20% is {} 30% is {}".format((i*10)/100,(i*20)/100, (i*30)/100))
#
# for i in range (10,0,-2):
#     print(i)


# import keyword
# print(keyword.kwlist)
# print("*"*60)
# print(dir())
# print(dir(__builtins__))

s1="ecoDers"

print(s1.capitalize())
print(s1.casefold())
print(s1.swapcase())
print(s1.upper())
print(s1.lower())
print(s1.isupper())
print(s1.islower())
print(len(s1))
print(s1.count("e"))
print(s1.startswith("e"))
print(s1.endswith("s"))
print(s1.find("D"))
print(s1.index("D"))
print(s1.rindex("D"))
print(s1.isalnum())
print(s1.isalpha())
print(s1.isnumeric())

s1="123"
print(s1.isnumeric())
print(s1.isdigit())
print(s1.isalnum())

s1="     "
print(s1.isalnum())
print(s1.isalpha())
print(s1.isnumeric())
print(s1.isdigit())
print(s1.isspace())

s1=""
print(s1.isalnum())
print(s1.isalpha())
print(s1.isnumeric())
print(s1.isdigit())

s1="This Is A Good Company"
print(s1.istitle())

usernsme= "     shiba......."
print(usernsme)
print(usernsme.lstrip(" "))
print(usernsme.rstrip("."))
print(usernsme.lstrip(" ").rstrip("."))

usernsme="shiba"
print(usernsme.ljust(20,"#"))
print(usernsme.rjust(20,"*"))

s1="hello welcome to skillmine"

s2=s1.split(" ")
print(s2)
print(len(s2))