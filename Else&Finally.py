print("Starting the program")
i=input("Please enter a number: ")
try:
    i=int(i)
    print(i)
except:
    print("You are in except right now cuz try didn't work")
else:
    print("Except not executed you are in else")
finally:
    print("Everything is completed and you are in finally")