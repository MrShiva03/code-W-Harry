
# print("%s to the right" % ("this is shiva"))

# print("this is a print statement 1", end= "")
# print("this is  print is statement 2")

# print("this "*5) 


# cities = ["japan", "america", "russia","australia","india"]
# heroes = ["jaguar", "amenda", "rupali","autrology","bakie"]

# def list_len(list):
#     print(len(list))
# print(cities)

# def print_list(list):
#     for item in list:
#         print(item, end=" ")

# print(list(heroes))
# print(list(cities))


def calculator():
    print("Simple Calculator")
    print("Operators: +, -, *, /, %, **")

    # take inputs
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator: ")

    # perform operation
    if op == '+':
        print("Result:", a + b)
    elif op == '-':
        print("Result:", a - b)
    elif op == '*':
        print("Result:", a * b)
    elif op == '/':
        print("Result:", a / b if b != 0 else "Error: Division by zero")
    elif op == '%':
        print("Result:", a % b)
    elif op == '**':
        print("Result:", a ** b)
    else:
        print("Invalid operator")

# run calculator
calculator()
