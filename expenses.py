# expenses.py
from input_utils import money

def expense():
    """Gathers monthly expenses from the user and calculates total expenses."""
    expenses = {}  # Dictionary to store expense names and costs

    print("How many expenses do you have per month: ")
    expenses_num = money()  # Get the number of expenses

    print(f"\nYou have {expenses_num} expenses.")
    
    for i in range(1, expenses_num + 1):  # Loop to get each expense
        print(f"\nWhat is the name of expense number {i}?")
        expense_name = input("Expense Name: ")  # Get expense name

        print(f"What is the cost of {expense_name}?")
        expense_cost = money()  # Get expense cost
        
        # Add the expense to the dictionary
        expenses[expense_name] = expense_cost

    # Display all entered expenses
    print("\nHere are your monthly expenses:")
    for expense_name, expense_cost in expenses.items():
        print(f"{expense_name}: ${expense_cost}")

    # Calculate and display the total of all expenses
    total_expenses = sum(expenses.values())
    print(f"\nYour total monthly expenses are: ${total_expenses}")
