# main.py
from input_utils import money
from expenses import expense
from user_managment import load_user_data, create_user, login

def main():
    print("Welcome to the main menu option")
    option_input = int(input("Option 1: Login \nOption 2: Create an account "))
    if (option_input == "login"):
        login()
    else if(option_input == ):
        create_user()
        
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
