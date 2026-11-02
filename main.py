import math_operations

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            continue

        if choice == '1':
            print(f"Result: {math_operations.add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {math_operations.subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {math_operations.multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {math_operations.divide(num1, num2)}")
    else:
        print("Invalid choice. Please pick an option from 1 to 5.")