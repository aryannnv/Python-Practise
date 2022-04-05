from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type="Rectangle"
    sides=4
    def __init__(self):
        self.breadth=4
        self.width=5
    def printarea(self):
        return self.breadth*self.width
r=Rectangle()
print(r.printarea())