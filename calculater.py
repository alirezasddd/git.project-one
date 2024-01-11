
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "zero error"


num1 = float(input("write your first number: "))
operator = input("enter the operator (+, -, *, /): ")
num2 = float(input("write your seconde number: "))


if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    result = "oprator is not definded"

print("your number: ", result)
