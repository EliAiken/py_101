def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

while True:
    print("Is your loan interest-free? (y/n) ")
    no_apr = input().strip().lower()
    if not no_apr:
        print("Please type 'y' for yes or 'n' for no.")
        continue
    if no_apr[0] == 'y':
        input("Great! Press Enter to continue ")
        APR = 0
        break
    elif no_apr[0] == 'n':
        while True:
            print("What is your monthly APR? (ex: type .05 for 5%) ")
            APR = input()
            if invalid_number(APR):
                print("Invalid number. Please try again with ONLY number "
                        "and decimal characters.")
            elif not invalid_number(APR):
                break
        break