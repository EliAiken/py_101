# Prompt for a bill amount and tip rate
# Program must compute tip, print both tip and amount of the bill
# Ignore input validation

print("Time to calculate the tip.")

print("What is the bill amount?")
bill_amount = float(input())

print("What is the tip percentage you want to give?")
tip_percentage = float(input())

print(f"""Calculating your tip...
      Your bill amount was ${bill_amount:.2f}
      Your tip percentage was ${tip_percentage:.2f}""")

tip_amount = bill_amount * (tip_percentage / 100)
bill_total = bill_amount + (bill_amount * (tip_percentage / 100))

print(f'The tip is ${tip_amount:.2f}')
print(f'The bill total is ${bill_total:.2f}')