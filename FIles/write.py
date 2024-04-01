# read the file and store all the line in list
# reverse and write back to list/file
# write the text back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
