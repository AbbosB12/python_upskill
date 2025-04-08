import numbers


def return_value():
    # print("This is a function")
    return 1000

print(return_value())


def return_integer() -> int:
    print("This is a function")

# return_integer()
print(return_integer())


print("---------------------------------")
# def cube(num) -> int: -> return type function

def cube(num: int) -> int:
    return num * num * num


print(cube(10))

print("---------------------------------")

#  def addition(num1,num2) -> numbers: -> using the general for the datatype

def addition(num1: numbers,num2: numbers,num3: numbers = 0, num4: numbers =0) -> numbers:
    return num1 + num2 +num3 + int(num4)


print(addition(10,1.99))
print(addition(10,1.99,89.98))
print(addition(10,1.99,89.98,"34"))


print("---------------------------------")


def function() -> int:
    pass