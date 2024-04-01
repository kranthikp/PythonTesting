# Python Basics
print("hello")

# here are the comments
a = 3
print(a)

# string variable
Str = "Hello World"
print(Str)

# multi variable assignment
b, c, d = 5, 6.4, "Great"
print(b, c, d)

# print("Value is " +b) #throws error type
print("{} {}".format("Value is", b))
print(Str+" "+d)

# variable type
print(type(b))
print(type(c))
print(type(d))

# Understanding Data Types

# List Datatype :Mutable -  allows multiple values and can be different data types
values = [1, 2, "panda", 4, 5]
print(values)

print(values[0])    # 1
print(values[1])    # 2

print(values[-1])   # panda
print(values[1:3])  # [2, 'panda']

values.insert(3,"kranthi")  # [1, 2, 'panda', 'kranthi', 4, 5]
print(values)

values.append("End")    # [1, 2, 'panda', 'kranthi', 4, 5, 'End']
print(values)

del values[0]
values[2] = "PANDA"     # Update # [2, 'PANDA', 'kranthi', 4, 5, 'End']
print(values)


# Tuple Datatype Same as List but Immutable - Cannot Update Existing Behaviour.
val = (1, 2, "panda", 4, 5)
print(val)

# val[2] = "PANDA"
# TypeError: 'tuple' object does not support item assignment

# Dictionary - Key Value Pair
dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic)
print(dic["c"])     # dic[key]
print(dic[4])

# how to create dictionary at run time
dict = { }
dict["firstname"] = "Kranthi"
dict["lastname"] = "Panda"
dict["gender"] = "Male"
print(dict)
print(dict["lastname"])
dict["firstname"] = "Kranthi Kumar" #udpate
print(dict)

del dict["gender"]
print(dict)
