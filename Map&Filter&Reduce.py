# MAP
# num=["2","7","9","16"]
# for i in range(len(num)):
#     num[i]=int(num[i])

# num=list(map(int,num))
# num[0]=num[0]+1
# print(num[0])

# num=[2,3,4,5,6,7,8,9]
# print(list(map(lambda x:x*x,num)))

# def sq(a):
#     return a*a
# def cube(a):
#     return a*a*a
# l=[sq,cube]
# for i in range(6):
#     a=list(map(lambda x:x(i),l))
#     print(a)

# FILTER
# n=[1,2,3,4,5,6,7,8,9]
# def gre(a):
#     return a>5
# gl=list(filter(gre,n))
# print(gl)

# REDUCE
from functools import reduce
l=[1,2,3,4]
s=reduce(lambda x,y:x+y,l)
print(s)