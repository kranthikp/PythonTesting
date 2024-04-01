it = 4

while it > 1:
    print(it)
    it = it - 1

print("while loop execution done")

it = 4
while it > 1:
    if it != 3:
        print(it)

    it = it - 1

print("while loop execution done")

it = 14
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)

    it = it - 1

print("while loop execution done")