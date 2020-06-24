import pytest
import random
import main

def test_hello_world():
  assert 'hello world' in main.hello_world().lower()
  
def test_add_int():
  a = 0
  b = 100
  for i in range(10):
    operand_one = random.randint(a,b)
    operand_two = random.randint(a,b)
    assert main.add(operand_one,operand_two) == operand_one+operand_two

def test_add_float():
  for i in range(10):
    operand_one = random.random()
    operand_two = random.random()
    assert main.add(operand_one,operand_two) == operand_one+operand_two
 
def test_rectangle():
  square = main.Square(6)
  assert square.area() == 36
  assert square.perimeter() == 24

  assert 'Rectangle' in str(main.Square.__mro__)
