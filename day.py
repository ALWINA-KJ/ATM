balance = 5000

amount = float(input("Enter amount to withdraw: "))

if amount <= balance:
    balance -= amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")# Variables
name = "Alwina"
