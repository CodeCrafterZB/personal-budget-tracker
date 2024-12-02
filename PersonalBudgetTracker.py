# Welcome message for the user
print("Welcome to Personal Budget Tracker!")

# Asking for the user's name and ensuring a default value if left empty
name = input("What is your name? ").strip()
if not name:
    name = "User"  # Default name if the user doesn't input anything
print(f"Hello, {name}! Let's manage your expenses wisely.")

# Prompting for a valid monthly budget
while True:
    budget = input(f"What's your total budget for this month, {name}? ₹")
# Checking if the input is a positive integer    
    if budget.isdigit() and int(budget) > 0:
        # Converting the valid input to an integer
        budget = int(budget)  
        break
    # Error message for invalid input
    print("Please enter a valid positive amount for your budget.")  # Error message for invalid input

print(f"Great! Let's track your expenses and ensure you stay within your budget of ₹{budget}.\n")

# Initializing an empty dictionary to store expenses
expenses = {}

# Main program loop for menu-based operations
while True:
    # Displaying the menu options to the user
    print("\nWhat would you like to do?")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. Delete an expense")
    print("5. Exit")
    
    # Taking the user's choice and validating it
    choice = input("Enter your choice (1-5): ").strip()
    if choice not in {"1", "2", "3", "4", "5"}:
        print("Invalid choice. Please choose a valid option.")
        continue

    # Option 1: Add an expense
    if choice == "1":
        category = input("Enter the expense category (e.g., Food, Transport): ").strip()
        if not category:
            print("Category cannot be empty. Please try again.")
            # Skipping the rest of this iteration if the category is invalid
            continue  

        while True:
            amount = input(f"How much did you spend on {category}? ₹")
            # Validating the amount
            if amount.isdigit() and int(amount) > 0:  # Validate the amount
# Convert the valid input to an integer
                amount = int(amount)
                break
# Error message for invalid amount
            print("Please enter a valid positive amount.")  

        # Adding the expense to the dictionary
        expenses[category] = expenses.get(category, 0) + amount
        print(f"Added ₹{amount} to {category}.")

    # Option 2: View all expenses
    elif choice == "2":
        if not expenses:
# Message if no expenses are recorded
            print("No expenses to show yet. Start adding some!")  
        else:
            print("\nHere are your expenses:")
            # Looping through the dictionary to display each expense
            for category, amount in expenses.items():  
                print(f"{category}: ₹{amount}")

    # Option 3: View total expenses
    elif choice == "3":
        # Calculating the total of all expenses
        total = sum(expenses.values())  
        print(f"\nTotal Expenses: ₹{total}")
        if total < budget:
            print(f"Good job, {name}! You're within your budget. Keep it up!")
        elif total == budget:
            print(f"Wow, {name}! You've exactly met your budget. Be cautious with future expenses.")
        else:
            print(f"Uh-oh, {name}! You've exceeded your budget by ₹{total - budget}. Consider cutting back on unnecessary expenses.")

    # Option 4: Delete an expense
    elif choice == "4":
        if not expenses:
            # Message if no expenses are recorded
            print("No expenses to delete yet. Add some first!")  
        else:
            category = input("Enter the category to delete: ").strip()
# Checking if the category exists in the dictionary
            if category in expenses:  
                # Deleting the category from the dictionary
                del expenses[category]  
                print(f"Deleted {category} from expenses.")
            else:
                print(f"{category} not found in expenses. Please try again.")

    # Option 5: Exit the program
    elif choice == "5":
        print(f"Goodbye, {name}! Happy budgeting. ")
        # Exiting the while loop and ending the program
        break  
