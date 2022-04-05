# f=open("lul.txt","rt")
#used for reading word by word
# c=f.read()
# print(c)
# c=f.read(10)
# print(c)

#for reading line by line
# for line in f:
#     print(line,end="")

# print(f.readline())
# print(f.readline())

# print(f.readlines())
# f.close()

# Seek and Tell
# f=open("lul.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# f.seek(9)
# print(f.readline())
# f.close()

# With Block
with open ("lul.txt") as f:
    a=f.readline()
    print(a)