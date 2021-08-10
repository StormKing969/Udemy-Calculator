def add(x, y):
    result = x + y
    return result


def divide(x, y):
    result = x / y
    return result


def multiply(x, y):
    result = x * y
    return result


def subtract(x, y):
    result = x - y
    return result


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter a number: "))
should_continue = True

while should_continue:
    operator = input("Enter the operator: ")
    num2 = int(input("Enter a number: "))
    print("")

    answer = operation.get(operator)(num1, num2)

    print(f"{num1} {operator} {num2} = {answer}")
    print("")

    choice = input(f"Press Q to quit else Press Enter")
    if choice.upper() != "Q":
        num1 = answer
    else:
        should_continue = False
