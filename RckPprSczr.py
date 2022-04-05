import random
n=10
cp=pp=0
op=['r','p','s']
name=input("Please Enter your name: ")
while(n):
    comp=random.choice(op)
    p=input("Please choose Rock Paper or Scizzor (r/p/s): ")
    n=n-1
    if comp=='r':
        if p=='p':
            pp=pp+1
        elif p=='s':
            cp=cp+1
    if comp=='p':
        if p=='s':
            pp=pp+1
        elif p=='r':
            cp=cp+1
    if comp=='s':
        if p=='r':
            pp=pp+1
        elif p=='p':
            cp=cp+1
print(f"The scores are Player: {pp} Computer: {cp}")
if pp>cp:
    print(f"Player {name} is the winner")
elif pp<cp:
    print("The Computer is the winner")
else:
    print("Its a tie")