ItemsInCart = 2
# 2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception("Product cart count not matching")
    pass

assert (ItemsInCart == 2)

# try, catch => except
try:
    with open('test1.txt', 'r') as reader:
        print(reader.read())

except:
    print("Some how reached this block")

# try, except with Python Exception
try:
    with open('test1.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    print(e)

# try, except with finally
try:
    with open('test.txt', 'r') as reader:
        print(reader.read())

except Exception as e:
    print(e)

finally:
    print("cleaning up records//")
