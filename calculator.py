import math

history = []

def calculator():
    while True:
        print("\n------ CALCULATOR ------")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (x^y)")
        print("6. Square root")
        print("7. Percentage")
        print("8. Show History")
        print("9. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input! Please enter a number from 1-9.")
            continue

        if choice == 1:  # Addition
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = x + y
            history.append(f"{x} + {y} = {result}")

        elif choice == 2:  # Subtraction
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = x - y
            history.append(f"{x} - {y} = {result}")

        elif choice == 3:  # Multiplication
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = x * y
            history.append(f"{x} * {y} = {result}")

        elif choice == 4:  # Division
            x = float(input("Enter numerator: "))
            y = float(input("Enter denominator: "))
            if y == 0:
                result = "Error! Division by zero."
            else:
                result = x / y
                history.append(f"{x} / {y} = {result}")

        elif choice == 5:  # Power
            x = float(input("Enter base: "))
            y = float(input("Enter exponent: "))
            result = math.pow(x, y)
            history.append(f"{x}^{y} = {result}")

        elif choice == 6:  # Square root
            x = float(input("Enter number: "))
            if x < 0:
                result = "Error! Cannot take square root of negative number."
            else:
                result = math.sqrt(x)
                history.append(f"√{x} = {result}")

        elif choice == 7:  # Percentage
            total = float(input("Enter total value: "))
            part = float(input("Enter part value: "))
            if total == 0:
                result = "Error! Total cannot be zero."
            else:
                result = (part / total) * 100
                history.append(f"{part} is {result}% of {total}")

        elif choice == 8:  # Show history
            print("\n------ Calculation History ------")
            if not history:
                print("No history yet.")
            else:
                for h in history:
                    print(h)
            continue

        elif choice == 9:  # Exit
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        print("Result:", result)


# Run calculator
calculator()
