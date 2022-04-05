d={"harry":"burger","rohan":"fish","ved":"taco","shubham":{"B":"upma","L":"chicken","D":"paneer"}}
# print(d["harry"])
# print(d["shubham"])
print(d)
d["putin"]="fries"
d["dimpu"]="nuggets"
print(d)
del d["dimpu"]
# d2=d.copy()
print(d)
print(d.get("harry"))
d.update({"leena":"toffee"})
print(d)
print(d.keys())
print(d.items())
inp=input("Please enter the name: ")
print(d.get(inp))
print(d[inp])
