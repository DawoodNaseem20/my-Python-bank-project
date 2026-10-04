#---User input check---
stored_pin = "12345"
account_name = "Dawood"
attempts_left = 3
balance = 50000
authentificated = False

print("="*45)
print("           Welcome To Python Bank!")
print("="*45)

#---Security check ---
while attempts_left > 0:
    entered_pin = input(f"\nEnter your Pin ({attempts_left} Attempts Left):")
    if entered_pin == stored_pin:
        print(f"\n--> Success! Welcome {account_name}!")
        authentificated =  True 
        break
    else:
        attempts_left = attempts_left - 1
        print("\nTry again!")
if not authentificated:
    print("\nSecurity Alert! 3 Wrong Attempts and card block!")
#---main menu of atm---
while authentificated:
    print("\n" + "="*35)
    print("1. Check your balance")
    print("2. Withdraw your balance")
    print("3. Deposite any amount")
    print("4. Exit!")
    choice = input("\nEnter a number (1-4):")

    #---conditional working---
    if choice=="1":
        print(f"\n--> Your Balance is: {balance:.2f}$")

    elif choice=="2":
        withdraw = float(input("\nEnter withdraw amount:$"))

        if withdraw > balance:
            print("Transaction Failed! Insufficient Amount!")
        elif withdraw <= 0:
            print("Invalid Withdrawl Amount!")
        else:   
            balance = balance - withdraw
            print(f"Transaction Successful! Your Balance is:${balance:.2f}")

    elif choice=="3":
        deposite=float(input("\nEnter deposite amount: $"))
        if deposite > 0:
            balance = balance + deposite
            print(f"\nSeccess! Your Current Balance is: {balance:.2f}$")
        else:
            print("INVALID AMOUNT! The amount will be greater than 0!")
    elif choice == "4":
        print("\nThankYou for using Python Bank!")
        break
    else:
        print("\nInvalid options!")        