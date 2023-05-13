fruits={"apple":"red colour",
        "orange":"orange colour",
        "mango":"red colour",
        "graps":"green colour",
        None:"yellow",
        "goava":None}
print(fruits)
print(type(fruits))
print(len(fruits))
print(fruits["apple"])
# print(fruits["red colour"]) we can fatch values through value
fruits["lichi"]="pink colour"
print(fruits)
print(len(fruits))
# print(fruits[0]) we can fatch values through index
print(fruits.keys())
print(fruits.values())
print(fruits.items())

veg={"potato":"yellow colour",
     "cucumber":"green"}
fruits.update(veg)
print(fruits)
print(veg)
print(fruits[None])
del fruits[None]
del fruits["goava"]
print(fruits)