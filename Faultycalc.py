while(True):
    a=int(input("Enter the 1st no: "))
    b=int(input("Enter the 2nd no: "))
    op=str(input("Enter the Operator: "))
    if a==45 and b==3 and op=='*':
        print("555")
    elif a==56 and b==9 and op=='+':
        print("777")
    elif a==56 and b==6 and op=='/':
        print("4")
    elif op=='*':
        print(a*b)
    elif op=='+':
        print(a+b)
    elif op=='-':
        print(a-b)
    elif op=='/':
        print(a/b)
    elif op=='%':
        print(a%b)
    elif op=='**':
        print(a**b)
    cont=input("Do you want to continue (y/n): ")
    if(cont=='n'):
        break