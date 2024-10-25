import json
import os
from input_utils import money
from expenses import expense

def load_user_data():
    """Load existing user data from the JSON file."""
    # Create the file users.json if it doesn't exist
    try:
        with open('users.json', 'r') as json_file:
            # Return the loaded user data as a dictionary
            return json.load(json_file)  # Use json.load to read the data
    except FileNotFoundError:
        # If the file doesn't exist, return an empty dictionary
        return {}

def create_user():
    """Save user data (username and password) to the JSON file."""
    while True:
        username = input("You are now creating a new account\nEnter a new username: ")  # Prompt for username
        password = input("Enter a new password: ")  # Prompt for password
        
        user_data = load_user_data()  # Load existing user data

        if username in user_data:
            print("Sorry, this username is already in use try again")

        else:
            # Promt for additional details
            try:
                saving = float(input("Enter your current savings amount: "))
                weekly_income = float(input("Enter your weekly income: "))

                #intialize a empty dictionary to hold all the expenses information
                expenses = {}
                add_expense = input("Do you want to add an expense? (Yes/No): ").lower()
                
                #Loop to add expenses if needed 
                while add_expense == "yes":
                    expense_name = input("Enter the expense name: ")
                    expense_amount = float(input(f"Enter the amount for {expense_name}: "))
                    expenses[expense_name] = expense_amount#adding key and item 
                    add_expense = input("Do you want to add anther expense? (Yes/No): ").lower()
                
                # Store user details in a dictionary
                user_info = {
                "password" : password,# Replace password with a hashed version in production
                "saving" : saving,
                "weekly_income" : weekly_income,
                "expenses": expenses}
                
                # Add user info dictionary to the main user_data dictionary
                user_data[username] = user_info  

                # Write updated user data back to the JSON file
                with open('users.json', 'w') as json_file:
                    json.dump(user_data, json_file)
                print("User data saved.")
                break
            except ValueError:
                print("Invalid input. Please enter numerical values for savings and income.")    

def login():
    """Check if the provided username and password match the stored user data."""
    user_data = load_user_data()  # Load existing data
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            # Check if the username exists and the password matches
            if username in user_data and user_data[username] == password:
                print("Login successful!")
                break  # Exit the loop on successful login
            else:
                print("Invalid username or password. Please try again.")
                # Ask for credentials again
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

