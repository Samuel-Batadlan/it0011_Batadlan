def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a % b

def summation(start, end):
    if start > end:
        print("Error: The second number must be greater than the first!")
        return None
    return sum(range(start, end + 1))

while True:
    print("\nMathematical Operations Menu")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

    choice = input("Enter your choice: ").upper()

    if choice == "Q":
        print("Exiting the program. Goodbye!")
        break

    if choice in ["D", "E", "R", "F"]:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))

            if choice == "D":
                result = divide(num1, num2)
            elif choice == "E":
                result = exponentiate(num1, num2)
            elif choice == "R":
                result = remainder(num1, num2)
            elif choice == "F":
                result = summation(num1, num2)

            if result is not None:
                print("Result:", result)

        except ValueError:
            print("Error: Please enter valid numbers!")

    else:
        print("Invalid choice! Please enter D, E, R, F, or Q.")
