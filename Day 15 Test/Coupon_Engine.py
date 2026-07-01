coupons = [

    {
        "code":"SAVE10",
        "type":"percent",
        "value":10,
        "min":0
    },

    {
        "code":"SAVE25",
        "type":"percent",
        "value":25,
        "min":2000
    },

    {
        "code":"FLAT150",
        "type":"flat",
        "value":150,
        "min":800
    },

    {
        "code":"FLAT500",
        "type":"flat",
        "value":500,
        "min":3000
    }

]

while True:

    while True:

        try:

            total=float(input("Cart Total : ₹"))

            if total<0:

                print("Enter Valid Total")

                continue

            break

        except:

            print("Enter Numeric Value")

    best_coupon=None

    best_discount=0

    for coupon in coupons:

        if total<coupon["min"]:

            continue

        if coupon["type"]=="percent":

            discount=total*coupon["value"]/100

        else:

            discount=coupon["value"]

        discount=min(discount,total)

        if discount>best_discount:

            best_discount=discount

            best_coupon=coupon

    if best_coupon:

        pay=total-best_discount

        print(f"\nBest Coupon : {best_coupon['code']}")

        print(f"Save : ₹{best_discount:.2f}")

        print(f"Pay : ₹{pay:.2f}")

    else:

        print("No Coupon Available")

    again=input("\nCheck Another?(y/n): ").lower()

    if again!="y":

        print("Program Closed")

        break