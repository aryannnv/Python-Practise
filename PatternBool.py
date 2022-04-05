inp=int(input("Please enter the no.: "))
bol=bool(int(input("Please Enter 0 or 1 for the pattern type: ")))
i=1
if bol==True:
    while(i<=inp):
        print("*"*i)
        i=i+1;
elif bol==False:
    while(inp):
        print("*"*inp)
        inp=inp-1