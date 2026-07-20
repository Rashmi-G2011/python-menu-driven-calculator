# Menu Driven Calculator with Exception Handling

while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Thank you! Exiting the program.")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", a + b)

        elif choice == 2:
            print("Result =", a - b)

        elif choice == 3:
            print("Result =", a * b)

        elif choice == 4:
            print("Result =", a / b)

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        print("An unexpected error occurred:", e)
