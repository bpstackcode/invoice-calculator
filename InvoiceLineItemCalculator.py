# ********************************************************
# Name: Bryan Peterson
# Class: CIS261
# Lab: Invoice Line Item Calculator
# Date: November 16, 2025
# ********************************************************

def get_price():
    """Get and validate a price from user input"""
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")


def get_quantity():
    """Get and validate a quantity from user input"""
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")


def main():
    print("The Invoice Line Item Calculator\n")

    while True:
        # Get valid price and quantity
        price = get_price()
        quantity = get_quantity()

        # Calculate total
        total = price * quantity

        # Display formatted result
        print(f"Price: {price:.2f}")
        print(f"Quantity: {quantity}")
        print(f"Total: {total:.2f}\n")

        # Ask user if they want to continue
        again = input("Enter another line item? (y/n): ").lower()
        if again != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    main()# Add your program code here.

print("Welcome to Invoice Line Item Calculator!")
