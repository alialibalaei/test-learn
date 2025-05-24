def add(first_number: float, second_number: float) -> float:
    """
    This function adds two numbers.
    """
    return first_number + second_number

def subtract(first_number: float, second_number: float) -> float:
    """
    This function subtracts the second number from the first number.
    """
    return first_number - second_number

def multiply(first_number: float, second_number: float) -> float:
    """
    This function multiplies two numbers.
    """
    return first_number * second_number

def get_number(prompt: str) -> float:
    """
    Gets a number from the user and ensures the input is valid.
    """
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except ValueError:
            print("Error: Please enter a valid number.")

def show_menu():
    """Displays the operation menu to the user."""
    print("\nSelect the desired operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Exit")

def run_calculator():
    """Main function to run the calculator program."""
    print("Super Simple Terminal Calculator")

    while True:
        show_menu()
        user_choice = input("Enter your choice (1-4): ")

        if user_choice == '4':
            print("Goodbye!")
            break

        if user_choice not in ('1', '2', '3'):
            print("Error: Invalid option. Please choose a number between 1 and 4.")
            continue

        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        result = None
        operation = ""

        if user_choice == '1':
            result = add(first_number, second_number)
            operation = "addition"
        elif user_choice == '2':
            result = subtract(first_number, second_number)
            operation = "subtraction"
        elif user_choice == '3':
            result = multiply(first_number, second_number)
            operation = "multiplication"

        if result is not None:
            print(f"The result of {operation} between {first_number} and {second_number} is: {result}")

if __name__ == "__main__":
    run_calculator()
