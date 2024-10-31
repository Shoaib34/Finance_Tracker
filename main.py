# main.py
from input_utils import money
from expenses import expense
from user_managment import load_user_data, create_user, login
from user_graph import display_user_graphs  # Import the graph display function

def main():
    print("Welcome to the main menu option")
    while True:
        try:
            option_input = int(input("Option 1: Login \nOption 2: Create an account \nOption: "))
            
            if option_input == 1:
                  # Call the login function
                display_user_graphs(login())  # Call the graph display function
               
                break
            elif option_input == 2:
                create_user()  # Call the create user function
                break
            else:
                print("Invalid option. Please choose 1 or 2.")  # Handle invalid input
                
        except ValueError:
            print("Invalid input! Please enter a numeric value.")  # Handle non-integer input
        except Exception as e:
            print(f"An error occurred, please choose 1 or 2: {e}")  # Handle any other exceptions



if __name__ == "__main__":
    main()
