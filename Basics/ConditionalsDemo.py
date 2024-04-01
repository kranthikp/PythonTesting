# Program Flow Control

# if block

greeting = "Good Morning"

if greeting == "Morning":
    print("Condition Matches")
    print("second line")
else:
    print("Condition do not Match")
print("if else completed")

print()
a = 4
if a > 2:
    print("4 greater than 2 Matches")
    print("second line")
else:
    print("num not greater than 2")
print("if else completed")

print()
# for Loop
print("### for Loop")
obj = [1, 2, 3, 4]
for i in obj:
    print(i)

print()
# for Loop
print("### for Loop")
obj1 = [1, 2, 3, 4]
for i in obj1:
    print(i*2)

print()
# Sum of First Natural numbers in list
print("### for Loop using range()")
summation = 0
obj1 = [1, 2, 3, 4, 5, 6, 7]
for j in range(1, 6):
    summation = summation + j
print(summation)

print()
# Sum of First Natural numbers in list
print("### for Loop using range(start, end-1, jump_index)")
summation = 0
obj1 = [1, 2, 3, 4, 5, 6, 7]

for k in range(1, 6, 2):
    print(k)
print("***********SKIPPING FIRST INDEX********")
for m in range(6):
    print(m)