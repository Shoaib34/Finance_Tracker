import json
import os

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

def create_user_data(username, password):
    """Save user data (username and password) to the JSON file."""
    user_data = load_user_data()  # Load existing user data

    # Add or update user data
    user_data[username] = password  # Replace password with a hashed version in production

    # Write updated user data back to the JSON file
    with open('users.json', 'w') as json_file:
        json.dump(user_data, json_file)
    print("User data saved.")

def login(username, password):
    """Check if the provided username and password match the stored user data."""
    user_data = load_user_data()  # Load existing data
    while True:
        try:
            # Check if the username exists and the password matches
            if username in user_data and user_data[username] == password:
                print("Login successful!")
                break  # Exit the loop on successful login
            else:
                print("Invalid username or password. Please try again.")
                # Ask for credentials again
                username = input("Enter your username: ")
                password = input("Enter your password: ")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

