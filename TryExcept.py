from logging import exception
from re import I


print("Enter no. 1")
a=input()
print("Enter no. 2")
b=input()
try:
    print("The sum of 2 nos is: ",int(a)+int(b))
except Exception as e:
    print(e)    
print("Very Important")