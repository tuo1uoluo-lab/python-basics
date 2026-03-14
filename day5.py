def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a ,b):
    return a * b
def divide(a, b):
    if b == 0:
        return "不能除以0"
    else:
        return a / b
num1 = 10
num2 = 5
operator = "/"
if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(subtract(num1, num2))
elif operator == "*":
    print(multiply(num1, num2))
elif operator == "/":
    print(divide(num1, num2))
