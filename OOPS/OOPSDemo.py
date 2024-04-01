# OOPS CONCEPTS - CLASSES AND OBJECTS

# Class - Class is a user defined blueprint or a prototype
# Example - A calculator used to ADD, SUBTRACT, MULTIPLY...
# A Class has methods, class variables, instance variables, constructors, etc

# Declaring a class in python
class Calculator:
    num = 100  # class variables

    # default constructor
    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print("I am called automatically when an object is created")

    def getData(self):
        print("Executing a getData Method of Calculator Class")

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num


# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword does not require when you create an object

obj = Calculator(2, 3)  # syntax to create obj in python
obj.getData()
print(obj.num)

obj1 = Calculator(4, 3)  # syntax to create obj in python
obj1.getData()
print(obj1.summation())

obj2 = Calculator(3, 7)  # syntax to create obj in python
obj2.getData()
print(obj2.summation())
