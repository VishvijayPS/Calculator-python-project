# Function to display the calculator menu
def display_menu():
    print("\nSimple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

# Function to perform the calculation
def perform_calculation(choice, num1, num2):
    if choice == '1':
        return num1 + num2
    elif choice == '2':
        return num1 - num2
    elif choice == '3':
        return num1 * num2
    elif choice == '4':
        if num2 == 0:
            return "Cannot divide by zero."
        return num1 / num2
    else:
        return "Invalid operation."

# Main function to run the calculator
def main():
    while True:
        display_menu()

        choice = input("Select operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Get two numbers from the user
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform calculation
        result = perform_calculation(choice, num1, num2)

        print(f"Result: {result}")

# Start the program
if __name__ == "__main__":
    main()
