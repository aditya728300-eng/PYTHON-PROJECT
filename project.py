# ADITYA KUMAR 
# ERP ID : RU-26-02615

menu = {"Dosa": 80, "Idli": 40, "Thali": 150, "Tea": 20}

def calculate_bill(cart):
    subtotal = 0
    for item, qty in cart.items():
        amount = menu[item] * qty
        subtotal += amount
        print(item, "x", qty, "| Amount:", amount)

    discount = subtotal * 0.10 if subtotal > 500 else 0
    gst = (subtotal - discount) * 0.05
    total = subtotal - discount + gst

    print("Subtotal:", f"{subtotal:.2f}")
    print("Discount:", f"{discount:.2f}") 
    print("GST(5%):", f"{gst:.2f}")
    print("Grand Total:", f"{total:.2f}")

def main():
    cart = {}

    while True:
        item = input("Enter item (or bill): ").strip().title()

        if item == "Bill":
            if cart:
                calculate_bill(cart)
            else:
                print("Cart is empty!")
            break

        if item not in menu:
            print("Item not on menu. Available: Dosa, Idli, Thali, Tea")
            continue

        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                print("Invalid quantity. Enter a number greater than 0.")
                continue
        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        cart[item] = cart.get(item, 0) + qty

main()
