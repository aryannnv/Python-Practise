class Employee:
    _protec=7
    __private=5
    leaves=10
    def __init__(self,aname,asal,arole):
        self.name=aname
        self.sal=asal
        self.role=arole
    def pr(self):
        return f"The Name is {self.name}, his role is {self.role} and his salary is {self.sal}"
    @classmethod
    def changeleaves(cls,l):
        cls.leaves=l
    @classmethod
    def fromdash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def pri(string):
        print("This is "+string)

# Single Inheritence
class Programmer(Employee):
    def __init__(self, aname, asal, arole,alang):
        self.name=aname
        self.sal=asal
        self.role=arole
        self.languages=alang
    def printprog(self):
        return f"The Name is of the programmer {self.name}, his role is {self.role} and his salary is {self.sal}, and the languages he uses are {self.languages}"

harry=Employee("Harry",100,"Teacher")
larry=Employee("Larry",10,"Student")
karan=Employee.fromdash("Karan-20-Student")
print(harry.leaves)
karan.pri("karan")
larry.changeleaves(5)
print(harry.leaves)
aman=Programmer("Aman","500","Programmer",["Python"])
chaman=Programmer("Chaman","777","Programmer",["Python","CPP","C"])
print(chaman.printprog())

# Public and Protected
print(harry._protec)
print(harry._Employee__private)

# Manual Setup
# harry=Employee()
# larry=Employee()
# harry.name="Harry"
# harry.sal=1000
# harry.role="Teacher"
# larry.name="Larry"
# larry.sal=50
# larry.role="Student"
# print(Employee.leaves)
# print(Employee.__dict__)
# Employee.leaves=5
# print(Employee.leaves)
# print(Employee.__dict__)