import json
import os

def load_user_data():
    """Load existing user data from the JSON file."""
    try:
        with open('users.json', 'r') as json_file:
            return json.load(json_file)  # Return loaded user data as a dictionary
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def get_float_input(prompt):
    '''Prompt the user for a float and validate input'''
    while True:
        try:
            return float(input(prompt))  # Prompt the user with the provided message
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_yes_no(prompt):
    '''Prompt the user for a yes or no answer'''
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response
        print("Invalid input. Please enter 'Yes' or 'No'.")

def add_expenses():
    """Prompt the user to add expenses to a dictionary."""
    expenses = {}
    
    while True:
        if get_yes_no("Do you want to add an expense? (Yes/No): ") == "yes":
            expense_name = input("Enter the expense name: ")
            expense_amount = get_float_input(f"Enter the amount for {expense_name}: ")
            expenses[expense_name] = expense_amount
        else:
            break  # Exit the loop if the user says "no"
    
    return expenses
    
def create_user():
    """Save user data (username and password) to the JSON file."""
    username = input("You are now creating a new account\nEnter a new username: ")
    
    user_data = load_user_data()  # Load existing user data
    while username in user_data:
        print("Sorry, this username is already in use. Try again.")
        username = input("Enter a new username: ")

    password = input("Enter a new password: ")
       
    saving = get_float_input("Enter your current savings amount: ")
    weekly_income = get_float_input("Enter your weekly income: ")
    expenses = add_expenses()
    
    # Store user details in a dictionary
    user_info = {
        "password": password,  # Replace password with a hashed version in production
        "saving": saving,
        "weekly_income": weekly_income,
        "expenses": expenses
    }
    
    # Add user info dictionary to the main user_data dictionary
    user_data[username] = user_info  

    # Write updated user data back to the JSON file
    with open('users.json', 'w') as json_file:
        json.dump(user_data, json_file, indent=4)  # Add indent for readability
    print("User data saved.")

def login():
    """Check if the provided username and password match the stored user data.
    
    Returns:
        dict: User data of the successfully logged-in user, or None if login fails.
    """
    user_data = load_user_data()  # Load existing data
    max_attempts = 3  # Set a limit for login attempts
    attempts = 0
    
    while attempts < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        if username in user_data and user_data[username]["password"] == password:
            print("Login successful!")
            return user_data[username]  # Return user data upon successful login
        else:
            attempts += 1
            print("Invalid username or password. Please try again.")
            if attempts == max_attempts:
                print("Too many failed attempts. Please try again later.")
                return None  # Return None if login fails after max attempts
