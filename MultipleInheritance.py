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
class Player:
    leaves=5
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame
    def printp(self):
        return f"The name is {self.name}, and the game he plays is {self.game}"
class CoolEmployee(Employee,Player):
    language="C++"
    def printe(self):
        return f"The language used is {self.language}"
harry=Employee("Harry",100,"Teacher")
larry=Employee("Larry",10,"Student")
karan=CoolEmployee("Karan",1000,"CoolProgrammmer")
print(karan.pr())
print(karan.printe())