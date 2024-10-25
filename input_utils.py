# input_utils.py
def money():
    """Handles input for monetary amounts, ensuring valid and non-negative values."""
    while True:
        try:
            value = int(input())  # Get user input
            if value < 0:  # Check for non-negative
                print("Sorry, you cannot input a negative number. Please try again.\n")
            else:
                return value
        except ValueError:
            print("Invalid input! \nPlease enter a numeric value.")
