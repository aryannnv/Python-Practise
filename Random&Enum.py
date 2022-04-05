import random
n=random.randint(0,10)
# print(n)
r=random.random()*100
# print(r)
l=["Mom","Dad","Sister","Brother","Mausi","Chicha"]
c=random.choice(l)
print(c)
for i,item in enumerate(l):
    if i%2==0:
        print(f"Family Member: {item}")