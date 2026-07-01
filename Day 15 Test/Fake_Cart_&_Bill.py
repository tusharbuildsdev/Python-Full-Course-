cart = {}

while True:

    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. View Cart")
    print("4. Checkout")

    choice = input("Choice: ")

    if choice == "1":

        name = input("Item Name: ")

        while True:
            try:
                price = float(input("Price: "))
                if price <= 0:
                    print("Price must be positive.")
                    continue
                break
            except:
                print("Enter a valid price.")

        while True:
            try:
                qty = int(input("Quantity: "))
                if qty <= 0:
                    print("Quantity must be positive.")
                    continue
                break
            except:
                print("Enter a valid quantity.")

        if name in cart:
            cart[name]["qty"] += qty
        else:
            cart[name] = {
                "price": price,
                "qty": qty
            }

        print("Item Added!")

    elif choice == "2":

        name = input("Item Name: ")

        if name in cart:
            del cart[name]
            print("Removed!")
        else:
            print("Not in cart.")

    elif choice == "3":

        if not cart:
            print("Cart Empty")
        else:

            for item, data in cart.items():

                amount = data["price"] * data["qty"]

                print(f"{item} x {data['qty']} = ₹{amount:.2f}")

    elif choice == "4":

        subtotal = 0

        for item, data in cart.items():

            subtotal += data["price"] * data["qty"]

        coupon = input("Coupon(blank for none): ")

        discount = 0

        if coupon == "SAVE10":

            discount = subtotal * 0.10

        elif coupon == "FLAT100" and subtotal >= 500:

            discount = 100

        gst = (subtotal - discount) * 0.18

        total = subtotal - discount + gst

        print("\n------ BILL ------")

        print(f"Subtotal : ₹{subtotal:.2f}")
        print(f"Discount : ₹{discount:.2f}")
        print(f"GST 18%  : ₹{gst:.2f}")
        print(f"TOTAL    : ₹{total:.2f}")

        break

    else:

        print("Invalid Choice")