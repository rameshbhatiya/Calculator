def calculator():
    print("----------------------------------------")
    print("           SIMPLE CALCULATOR            ")
    print("----------------------------------------")

    while True:
        try:
            number1 = float(input("Enter number 1: "))
            number2 = float(input("Enter number 2: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.\n")
            continue

        sign = input("Enter any sign (+, -, *, /, %) or type 'q' to quit: ").strip()

        if sign.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if sign == '+':
            result = number1 + number2
            print(f"Result: {number1} + {number2} = {result}\n")
        elif sign == '-':
            result = number1 - number2
            print(f"Result: {number1} - {number2} = {result}\n")
        elif sign == '*':
            result = number1 * number2
            print(f"Result: {number1} * {number2} = {result}\n")
        elif sign == '/':
            if number2 == 0:
                print("Error! Division by zero is not allowed.\n")
            else:
                result = number1 / number2
                print(f"Result: {number1} / {number2} = {result}\n")
        elif sign == '%':
            if number2 == 0:
                print("Error! Division by zero is not allowed for percentage.\n")
            else:
                result = (number1 / number2) * 100
                print(f"Result: {number1} is {result}% of {number2}\n")
        else:
            print("Invalid sign! Please enter a valid operator (+, -, *, /, %).\n")

if __name__ == "__main__":
    calculator()
