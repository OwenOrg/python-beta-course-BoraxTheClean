def hello_world():
  return "HeLlO WORLd!!!11"
  
def add(a,b):
  return a+b

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
        super().__init__(length,length) #Fill Me In
