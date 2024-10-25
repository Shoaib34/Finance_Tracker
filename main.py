# main.py
from input_utils import money
from expenses import expense
from user_managment import load_user_data, create_user, login

def main():
    print("Welcome to the main menu option")
    while True:
        try:
            option_input = int(input("Option 1: Login \nOption 2: Create an account \nOption: "))
            
            if option_input == 1:
                login()  # Call the login function
            elif option_input == 2:
                create_user()  # Call the create user function
            else:
                print("Invalid option. Please choose 1 or 2.")  # Handle invalid input
                
        except ValueError:
            print("Invalid input! Please enter a numeric value.")  # Handle non-integer input
        except Exception as e:
            print(f"An error occurred, please choose 1 or 2: {e}")  # Handle any other exceptions


    # Ask the user for initial saved money
    print("How much money do you currently have saved up? ")
    initial_savings = money()
    print(f"You have ${initial_savings} saved up.\n")

    # Ask the user for their weekly income
    print("What is your weekly income?")
    weekly_income = money()
    print(f"Your weekly income is ${weekly_income}.\n")

    # Now, run the expense function to gather expenses
    expense()

if __name__ == "__main__":
    main()
