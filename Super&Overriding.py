class A:
    classvar="I am a variable in class A"
    def __init__(self):
        self.var="I am inside class A's constructor"
        self.classvar="I am an instance of class A"
        self.special="Special"
class B(A):
    classvar="I am a variable in class B"
    def __init__(self):
        self.var="I am inside class B's constructor"
        self.classvar="I am an instance of class B"
        super().__init__()
a=A()
b=B()
print(b.classvar)