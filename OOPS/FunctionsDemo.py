# Functions - a group of related statements that performs a specific task
# whenever a functions are used wrapped under a class is called methods

# Simple Function
def greetMe():  # Function Declaration
    print("Good Day !!")


greetMe()  # Function Call


# Parameterized Function
def greetMe(name):  # Function Declaration
    print("Hey " + name + " Have a Good Day !!")


greetMe("Kranthi!")  # Function Call


def AddIntegers(a, b):
    return a + b


print(AddIntegers(2,10))