"""Case Study 13: ATM Transaction Sequence Simulation
Simulate a sequence of deposits and withdrawals while checking available balance.
"""

balance = float(input("Starting balance (₹): "))
count = int(input("Number of transactions: "))

if balance < 0 or count < 0:
    print("Invalid starting balance or transaction count.")
else:
    for i in range(count):
        transaction_type = input(f"Transaction {i + 1} (deposit/withdraw): ").strip().lower()
        amount = float(input("Amount (₹): "))

        if amount < 0:
            print("Invalid amount.")
        elif transaction_type == "deposit":
            balance += amount
            print("Deposit successful.")
        elif transaction_type == "withdraw":
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Unknown transaction type.")

        print(f"Current balance: ₹{balance:.2f}")

    print(f"Final balance: ₹{balance:.2f}")
