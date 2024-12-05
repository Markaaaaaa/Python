inventory=[
    {"id": 1, "name": "laptop", "price": 1399.99},
    {"id": 2, "name": "Airpods", "price": 249.00},
    {"id": 3, "name": "speaker", "price": 59.99},
    {"id": 4, "name": "iphone 13", "price": 599.69},
    {"id": 5, "name": "Ac Adapter", "price": 99.99},
]
cart = []

def display_store():
    print("\nAvailable Products:")
    for product in inventory:
        print(f"ID: {product['id']}, Name: {product['name']}, Price: ${product['price']:.2f}")


def add_to_cart():
        product_id = int(input("\nEnter the product ID to add to the cart: "))
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        product = next((p for p in inventory if p["id"] == product_id), None)
        if product:
            cart_item = next((item for item in cart if item["id"] == product_id), None)
            if cart_item:
                cart_item["quantity"] += quantity
            else:
                cart.append(
                    {"id": product["id"], "name": product["name"], "price": product["price"], "quantity": quantity})
            print(f"Added {quantity} of {product['name']} to the cart.")
        else:
            print("Product not found.")

def view_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    print("\nYour Shopping Cart:")
    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Total: ${item_total:.2f}")
    print(f"Cart Total: ${total:.2f}")

def remove_from_cart():
    try:
        product_id = int(input("\nEnter the product ID to remove from the cart: "))
        cart_item = next((item for item in cart if item["id"] == product_id), None)
        if cart_item:
            cart.remove(cart_item)
            print(f"Removed {cart_item['name']} from the cart.")
        else:
            print("Product not found in the cart.")
    except ValueError:
        print("Invalid input. Please enter a valid product ID.")

def complete_purchase():
    if not cart:
        print("\nYour cart is empty. Add items before completing the purchase.")
      return

    total = sum(item["price"] * item["quantity"] for item in cart)
    print(f"\nYour total is ${total:.2f}")
    confirm = input("Do you want to proceed with the purchase? (yes/no): ").strip().lower()
    if confirm == "yes":
        print("Purchase successful! Thank you for shopping.")
        cart.clear()
    else:
        print("Purchase canceled.")

def menu():
    while True:
        print("\nMenu:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Remove from Cart")
        print("5. Complete Purchase")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_store()
            elif choice == 2:
                add_to_cart()
            elif choice == 3:
                view_cart()
            elif choice == 4:
                remove_from_cart()
            elif choice == 5:
                complete_purchase()
            elif choice == 6:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

menu()
