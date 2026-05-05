def calc():
    try:
        a = int(input("Enter the first num: "))
        b = int(input("Enter the second num: "))
    except ValueError:
        print("Invalid input! Please enter integers.")
        return

    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        print("SUM =", a + b)
    elif operation == "-":
        print("DIFFERENCE =", a - b)
    elif operation == "*":
        print("PRODUCT =", a * b)
    elif operation == "/":
        try:
            print("QUOTIENT =", a / b)
        except ZeroDivisionError:
            print("Error: Denominator cannot be 0")
    else:
        print("INVALID OPERATION")


if __name__ == "__main__":
    calc()