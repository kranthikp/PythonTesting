file = open('test.txt')
# Read all the content of the file
# print(file.read())

# read n number of characters by passsing parameter
# print(file.read(7))

# read one single line at a time using readline()
# print(file.readline())
# print(file.readline())

# Print line by line using readLine method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()


for line in file.readlines():
    print(line)

    
file.close()
