import random

otp = None
attempts = 0

while True:
    print("\n--------- OTP MENU ------")
    print("1. Send OTP")
    print("2. Enter OTP")
    print("3. Exit")

    choice = input("choice: ")

    if choice == "1":
        otp = random.randint(10000000, 99999999)
        attempts = 3

        print(f"[SMS] Your OTP is {otp}")

    elif choice == "2":
        if otp is None:
            print("No OTP sent yet.")
            otp= None
            continue

        user_otp = input("Enter OTP: ")

        if not user_otp.isdigit() or len(user_otp) != 6:
            print("Enter a valid 6-digit code.")
            continue

        if int(user_otp) == otp:

            print("Verified!")

            otp = None
            attempts = 0

        else:

            attempts -= 1

            if attempts>0:
                print(f"Wrong OTP. Attempts Left: {attempts}")

            else:
                print("OTP expired.")
                otp = None

    elif choice == "3":
        print("Program Closed.")
        break


    else:
        print("Invalid choice.")