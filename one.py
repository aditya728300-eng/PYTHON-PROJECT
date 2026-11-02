"""Command-line restaurant billing program."""
# ADITYA KUMAR
# RU-26-02615


from decimal import Decimal
from typing import Dict


MENU = {"Dosa": 80, "Idli": 40, "Thali": 150, "Tea": 20}


def calculate_bill(cart: Dict[str, int]) -> None:
    subtotal = Decimal("0")
    for item, quantity in cart.items():
        amount = Decimal(MENU[item]) * quantity
        subtotal += amount
        print(item, "x", quantity, "| Amount:", f"{amount:g}")

    discount = subtotal * Decimal("0.10") if subtotal > 500 else Decimal("0")
    gst = (subtotal - discount) * Decimal("0.05")
    total = subtotal - discount + gst

    print("Subtotal:", f"{subtotal:.2f}")
    print("Discount:", f"{discount:.2f}")
    print("GST(5%):", f"{gst:.2f}")
    print("Grand Total:", f"{total:.2f}")


def main() -> None:
    cart: Dict[str, int] = {}

    while True:
        item = input("Enter item (or bill): ").strip().title()

        if item == "Bill":
            if cart:
                calculate_bill(cart)
            else:
                print("Cart is empty!")
            break

        if item not in MENU:
            print("Item not on menu. Available: Dosa, Idli, Thali, Tea")
            continue

        try:
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Invalid quantity. Enter a number greater than 0.")
                continue
        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        cart[item] = cart.get(item, 0) + quantity


if __name__ == "__main__":
    main()
