balance = 0
history = []

while True:

    print("\n------ WALLET ------")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Mini Statement")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        while True:

            try:

                amount = float(input("Enter Amount: "))

                if amount <= 0:
                    print("Amount must be positive.")
                    continue

                break

            except:
                print("Enter Valid Amount.")

        balance += amount

        history.append(("DEPOSIT", amount, balance))

        print(f"Current Balance : ₹{balance:.2f}")

    elif choice == "2":

        while True:

            try:

                amount = float(input("Enter Amount: "))

                if amount <= 0:
                    print("Amount must be positive.")
                    continue

                break

            except:
                print("Enter Valid Amount.")

        if amount > balance:

            print("Insufficient Balance.")

        else:

            balance -= amount

            history.append(("WITHDRAW", amount, balance))

            print(f"Current Balance : ₹{balance:.2f}")

    elif choice == "3":

        if not history:

            print("No Transactions Yet.")

        else:

            print("\n------ MINI STATEMENT ------")

            for transaction in history:

                t_type = transaction[0]
                amount = transaction[1]
                bal = transaction[2]

                print(f"{t_type:<10} ₹{amount:.2f}    Balance ₹{bal:.2f}")

            print(f"\nCurrent Balance : ₹{balance:.2f}")

    elif choice == "4":

        print("Thank You!")

        break

    else:

        print("Invalid Choice")