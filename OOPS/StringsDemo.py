Str = "Panda Automation"

print(Str[1]) # a

print(Str[0:5]) # Panda - way to get sub string

str2 = "Kranthi"
print(Str+" "+str2) # concatenation

str3 = "Panda"

print(str3 in Str) # True 'in' keyword

# split
str4 = "  pandaautomation.com  "
var = str4.split(".")
print(var) # ['pandaautomation', 'com']
print(var[0])

# trim - to trim whitespace from string
print(str4.strip())
print(str4.lstrip())
print(str4.rstrip())

