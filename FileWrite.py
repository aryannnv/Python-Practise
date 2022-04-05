# f=open("lul.txt","w")
# f.write("Aryan is Champion")
# f.close()
# f=open("lul.txt","a")
# a =f.write("Aryan is the best\n")
# print(a)
# f.close()

# Both read and write
f=open("lul.txt","r+")
print(f.read())
f.write("Amazing\n")
f.close()