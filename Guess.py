from pip import main


n=25
guess=9
print("And the name is: ",__name__)
if __name__=='__main__':
    while(guess):
        no=int(input("Guess the number: "))
        if no==n:
            print("Your guess is correct. No. of guesses taken: ",10-guess)
            break
        elif no>n:
            guess=guess-1
            print("Number is smaller")
        else:
            guess=guess-1
            print("Number is bigger")
        print("Guesses left: ",guess)