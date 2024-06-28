while True:    
    print("Would you like to calculate another car payment? (y/n)")
    answer = input().strip().lower()
    if answer[0] == 'n':
        print("Thank you, have a nice day!")
        break
    elif answer[0] != 'y':
        print("Please type y for 'yes' or n for 'no'.")
    else:
        break