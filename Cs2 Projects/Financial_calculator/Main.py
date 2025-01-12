
#Aaron.Wang Financial Calculator
import time

def TIME():
    """
    a loading with a short delay.
    """
    print("Loading...")
    time.sleep(1)

def main():
    """
    Main function to handle user choice .
    """
    while True:
        print("Welcome to the Financial Calculator!")
        TIME()
        print("1. Savings Goal Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")
        choice = input("Select an option 1-6: ")

        if choice == "1":
            saving_goal_calculator()
        elif choice == "2":
            compound_interest_calculator()
        elif choice == "3":
            budget_allocator()
        elif choice == "4":
            sale_price_calculator()
        elif choice == "5":
            tip_calculator()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

def saving_goal_calculator():
    """
    Calculates the time needed to save for a goal based on Weekly or monthly deposits.
    """
    print("Savings Goal Calculator is now ready to go!")
    goal = float(input("How much is your goal?: $"))
    deposit = float(input("How much would you deposit Weekly or Monthly?: $"))
    period = input("Is it weekly or monthly?: ").lower()

    if period == "weekly":
        months = goal / deposit / 4
    elif period == "monthly":
        months = goal / deposit
    else:
        print("Invalid. Please try again.")
        return

    print(f"It will take about {months:.2f} months to reach your savings goal.")

def compound_interest_calculator():
    """
    Calculates compound interest, rate, and time.
    """
    print("This is the Compound Interest Calculator!")
    principal = float(input("How much money do you have in the bank?: $"))
    rate = float(input("Enter the annual interest rate in % ")) / 100
    years = int(input("Enter the time in years: "))

    future_value = principal * (1 + rate) ** years
    print(f"The future value of your investment is: ${future_value:.2f}")

def budget_allocator():
    """
    income into predefined spending categories.
    """
    print("This is the Budget Allocator!")
    income = float(input("enter your monthly income $"))

    savings = 0.20 * income
    entertainment = 0.10 * income
    food = 0.30 * income
    others = 0.40 * income

    print("This is your budget:")
    TIME()
    print(f"Save this much money: ${savings:.2f}")
    TIME()
    print(f"Spend on entertainment: ${entertainment:.2f}")
    TIME()
    print(f"Spend on food: ${food:.2f}")
    TIME()
    print(f"spend on other items: ${others:.2f}")

def sale_price_calculator():
    """
    calculates the sale price after a discount.
    """
    original_price = float(input("Enter the original price:"))
    TIME()
    discount = float(input("Enter the discount percentage:")) / 100
    TIME()
    sale_price = original_price * (1 - discount)

    print(f"The sale price is ${sale_price:.2f}")

def tip_calculator():
    """
    Calculates the tip and total bill amount.
    """
    bill = float(input("Enter the bill amount: $"))
    TIME()
    tip_percentage = float(input("Enter the tip percentage: ")) / 100

    tip = bill * tip_percentage
    total = bill + tip

    print(f"Tip: ${tip:.2f}, Total bill: ${total:.2f}")

# Run the program
main()
