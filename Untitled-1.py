#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 17:02:08 2025

@author: wangqinghu
"""

# Financial Calculator Program
import time
def TIME():
    print("Loding...")
    time.sleep(1)
def main():
    """
    Main function to handle user chouice.
    """
    while True:
        print("Welcome to the Financial Calculator!")
        print("1. Savings Goal Calculator")
        print("2. Compound Interest Calculator")
        print("3. Budget Allocator")
        print("4. Sale Price Calculator")
        print("5. Tip Calculator")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
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
            print("Please try again.")
#saving goal calculator
def saving_goal_calculator():
    print("Saving Goal Calculator is now ready to go!")
    goal = float(input("How much is your goal?:"))
    deposit = float(input("How much would you deposit Weelky ot monthly?:"))
    weak_or_month = input("is it weekly or monthly?:")
    if weak_or_month == "weekly":
        time = goal / deposit / 4
    elif weak_or_month == "monthly":
        time = goal / deposit
    else:
        print("Invalid. Try again.")
        return
    print(f"It will take about {time:.2f} months to reach your savings goal.")
#compind interst calculator
def compound_interest_calculator():
    print("This is the compound interest calvulator!")
    money_in_bank = float(input("Hi!, how much money do you now have in your bank?:"))
    rate = float(input("Enter the annual interest rate (in %): ")) / 100
    time = int(input("Enter the time in years: "))
    future_money = money_in_bank * (1 + rate) ** (1 * time)
    print(f"The future money of your investment is: ${future_money:.2f}")
    #budget_allocator
def budget_allocator():
    print("This is the budget allocator!")
    income = float(input("Enter your monthly income:"))
    Savings = 0.20
    Want_to_buy = 0.10
    food = 0.30
    others =  0.40
    print("This is your budget")
    time
    print(f"Save this much money: {income * Savings:.2f}$")
    TIME
    print(f"This is how much to spend for what you wnat to buy:{income * Want_to_buy}$")
    print(f"How much for food?:{income * food}$")
    print(f"This is how much for other stuffs{income * others}$")
    #sale_price_calculator
def sale_price_calculator():

    original_price = float(input(" what is the original price: $"))
    discount = float(input("what is the discount percentage: ")) / 100   
    sale_price = original_price * (1 - discount)
    print(f"the price is: ${sale_price:.2f}")
    #tip_calculator
def tip_calculator():
    bill = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage: ")) / 100
    
    tip = bill * tip_percentage
    total = bill + tip
    print(f"tip: ${tip:.2f}, total bill: ${total:.2f}")
main()

    
