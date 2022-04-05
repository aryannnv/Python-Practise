# def fact(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# inp=int(input("Factorial No: "))
# print("Factorial Of",inp,":",fact(inp))
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
inp=int(input("Please enter the fibonacci no: "))
print("The no at the position",inp,":",fib(inp))