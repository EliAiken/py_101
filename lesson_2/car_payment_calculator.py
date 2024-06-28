import time

import sys

def prompt(message):
    print(f">>> {message} <<<")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

while True:
    prompt("Welcome to Eli's Car Payment Calculator!")
    print("""
        _____
     __//_||_\\_____
    |______________|
   ____0________0_____
          """)
    input("Press Enter to continue ")

    prompt("To calculate your monthly payment, we will need your "
        "car loan information.")
    input("Press Enter to continue ")
    while True:
        prompt("What is the amount of your loan? ")
        loan_amount = input()
        
        if not invalid_number(loan_amount):
            break

        prompt("Invalid number. Please try again with ONLY number characters.")

    prompt("Is your loan interest-free? (y/n) ")
    no_apr = input().strip().lower()
    if no_apr[0] == 'y':
        input("Great! Press Enter to continue ")
        APR = 0
    if no_apr[0] == 'n':
        while True:
            prompt("What is your monthly APR? (ex: type .05 for 5%) ")
            APR = input()

            if not invalid_number(APR):
                break

    while True:
        prompt("What is your loan duration in months? ")
        loan_duration = input()

        if not invalid_number(loan_duration):
            break

        prompt("Invalid number. Please try again with ONLY number characters.")

    loan_amount = float(loan_amount)
    APR = float(APR)
    loan_duration = float(loan_duration)
    if APR:
        monthly_apr = APR / 12
        monthly_payment = loan_amount * (monthly_apr / (1 - (1 + monthly_apr) ** (-loan_duration)))
    else:
        monthly_payment = loan_amount / loan_duration
    prompt("Thank you for the information. Please wait while we calculate "
           "your monthly payment...")
    time.sleep(5)
    rounded_payment = round(monthly_payment, 2)
    prompt(f"Your monthly car payment will be: ${rounded_payment}")
    
    prompt("Would you like to calculate another car payment? (y/n)")
    answer = input().strip().lower()
    if answer[0] == 'n':
        prompt("Thank you, have a nice day!")
        print("""
           _____
        __//_||_\\_____
  $$$$$|______________|
      ____0________0_____
        """)
        break