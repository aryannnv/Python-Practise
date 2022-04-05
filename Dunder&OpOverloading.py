from pydoc import apropos


class Employee:
    leaves=10
    def __init__(self,aname,asal,arole):
        self.name=aname
        self.sal=asal
        self.role=arole
    def pr(self):
        return f"The name is {self.name}, and the role is {self.role} with salary {self.sal}"
    def __add__(self,other):
        return self.sal+other.sal
    def __truediv__(self,other):
        return self.sal/other.sal
    def __repr__(self):
        return f"Employee('{self.name}','{self.role}','{self.sal}')"
    # def __str__(self):
    #     return f"The name is {self.name}, and the role is {self.role} with salary {self.sal}"
    @classmethod
    def changel(self,newl):
        self.leaves=newl
emp1=Employee("Harry",500,"Programmer")
emp2=Employee("Ligga",100,"Cleaner")
print(str(emp1))