def hello_world():
  #TODO
  
def add(a,b):
  #TODO

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Square(Rectangle):
    def __init__(self,length):
        super().__init__() #Fill Me In
