import matplotlib.pyplot as plt

def display_user_graphs(user_info):
    # Extract data for plotting
    savings = user_info['saving']
    weekly_income = user_info['weekly_income']
    expenses = user_info['expenses']
    total_expenses = sum(expenses.values())

    # Prepare data for the graph
    labels = ['Savings', 'Weekly Income', 'Total Expenses']
    values = [savings, weekly_income, total_expenses]

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=['green', 'blue', 'red'])
    
    # Adding titles and labels
    plt.title('User Financial Breakdown')
    plt.xlabel('Categories')
    plt.ylabel('Amount ($)')
    #lowest lim = 0, take the max value from values and 500 to it
    plt.ylim(0, max(values) + 500)  # Set y-axis limit for better visibility

    # Show value labels on top of the bars
    #enumerate returns both index and actual value
    for i, value in enumerate(values):
        #i = x coordinate
        plt.text(i, value + 10, f"${value}", ha='center')

    plt.grid(axis='y')  # Add grid for better readability
    plt.show()

    # Optionally, you could also add a pie chart for visual diversity
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('User Financial Breakdown - Pie Chart')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    plt.show()
