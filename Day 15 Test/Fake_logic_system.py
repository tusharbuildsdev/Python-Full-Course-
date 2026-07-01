users = {
    "aditi": "pass123",
    "rahul": "hunter2"
}

attempts = {}
locked = set()

while True:

    username = input("Username: ").strip()

    if not username:
        print("Username cannot be empty.\n")
        continue

    password = input("Password: ").strip()

    if not password:
        print("Password cannot be empty.\n")
        continue

    #Locked account?
    if username in locked:
        print("Account locked!")
        break

    #User exists
    if username not in users:
        print("No such user.\n")
        continue

    #Correct password
    if users[username] == password:
        print("Login successful!")
        break

    # Wrong password
    attempts[username] = attempts.get(username, 0) + 1

    if attempts[username] >= 3:
        locked.add(username)
        print("Account locked!")
        break
    else:
        left = 3 - attempts[username]
        print(f"Wrong password. Tries left: {left}\n")