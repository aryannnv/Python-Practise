class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    @property # For removing () from function calling statement at line 9,11
    def email(self):
        if self.fname==None or self.lname==None:
            return("Email not set. Please set it up using the setter")
        return f"{self.fname}.{self.lname}@codewithharry.com"
    @email.setter
    def email(self,string):
        print("Setting Now.....")
        name=string.split("@")[0]
        self.fname=name.split(".")[0]
        self.lname=name.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None
p=Employee("Harry","Sharma")
print(p.email)
p.fname="Jogindhar"
print(p.email)
p.email="harry.singh@codewithharry.com"
print(p.fname)
del p.email
print(p.email)
p.mail="aryan.champion@coderboy.com"
print(p.mail)
# print(type(p))
# print(id(p))
# print(dir(p))
import inspect
# print(inspect.getmembers(p))