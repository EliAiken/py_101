import time
import os
import math

def prompt(message):
    print(f">>> {message} <<<")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f'Value must be > 0: {number_str}')
        if math.isnan(number):
            return True
        if math.isinf(number):
            return True
    except ValueError:
        return True

    return False

CONTINUE_PROGRAM = True

while CONTINUE_PROGRAM:
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

        prompt("Invalid number. Please try again with ONLY "
               "postive number characters.")

    while True:
        prompt("Is your loan interest-free? (y/n) ")
        no_apr = input().strip().lower()
        if not no_apr:
            prompt("Please type 'y' for yes or 'n' for no.")
            continue

        if no_apr not in ['y', 'yes', 'n', 'no']:
            prompt("Please type 'y' for yes or 'n' for no.")
            continue

        if no_apr in ['y', 'yes']:
            input("Great! Press Enter to continue ")
            APR = 0
            break

        if no_apr in ['n', 'no']:
            while True:
                prompt("What is your monthly APR? (example: put .05 for 5%) ")
                APR = input()
                if invalid_number(APR) or APR.isdigit():
                    prompt("Invalid number. Your monthly APR must start with "
                           "a decimal character and ONLY include "
                           "positive integers.")
                elif not invalid_number(APR):
                    break
            break

    while True:
        prompt("What is your loan term (in months)? ")
        loan_duration = input()

        if not invalid_number(loan_duration):
            break

        prompt("Invalid number. Please try again with ONLY "
               "positive number characters.")

    loan_amount = float(loan_amount)
    APR = float(APR)
    loan_duration = float(loan_duration)

    if APR:
        monthly_apr = APR / 12
        monthly_payment = loan_amount * (
            monthly_apr /
            (1 - (1 + monthly_apr) ** (-loan_duration)))
    else:
        monthly_payment = loan_amount / loan_duration

    prompt("Thank you! Please wait while we calculate "
           "your monthly payment...")
    print(f""">>> Your loan info included: <<<
           Loan Amount: ${int(loan_amount)}
           APR: {int(APR * 100)}%
           Loan Term: {int(loan_duration)} months""")
    time.sleep(5)
    prompt(f"Your monthly car payment will be: ${monthly_payment:.2f}")

    while True:
        prompt("Would you like to calculate another car payment? (y/n)")
        answer = input().strip().lower()
        if not answer:
            prompt("Please type 'y' for yes or 'n' for no.")
            continue

        if answer not in ['y', 'yes', 'n', 'no']:
            prompt("Please type 'y' for yes or 'n' for no.")
            continue

        if answer in ['y', 'yes']:
            os.system('clear')
            break

        if answer in ['n', 'no']:
            prompt("Thanks for using Eli's Car Payment Calculator! Have "
                   "a nice day!")
            print("""
                 _____
              __//_||_\\_____
        $$$$$|______________|
        ________0________0______
            """)
            CONTINUE_PROGRAM = False
            break