special = "!@#$%^&*"

while True:

    password = input("Enter Password: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_length = False

    if len(password) >= 8:
        has_length = True

    for ch in password:

        if ch.isupper():
            has_upper = True

        elif ch.islower():
            has_lower = True

        elif ch.isdigit():
            has_digit = True

        elif ch in special:
            has_special = True

    score = 0

    if has_length:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_digit:
        score += 1

    if has_special:
        score += 1

    if score == 5:
        verdict = "Strong"

    elif score >= 3:
        verdict = "Medium"

    else:
        verdict = "Weak"

    missing = []

    if not has_length:
        missing.append("Length should be at least 8")

    if not has_upper:
        missing.append("Uppercase Letter")

    if not has_lower:
        missing.append("Lowercase Letter")

    if not has_digit:
        missing.append("Digit")

    if not has_special:
        missing.append("Special Character")

    print(f"\nScore : {score}/5 -> {verdict}")

    if missing:
        print("Missing :")

        for rule in missing:
            print("-", rule)

    else:
        print("All Rules Passed!")

    again = input("\nCheck another? (y/n): ").lower()

    if again != "y":
        print("Program Closed")
        break