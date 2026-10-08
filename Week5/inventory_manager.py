import os
import json

#Each product is a dictionary; the inventory is a list of dictionaries.
# Example of what the inventory list looks like:
# [
#     {"id": "P001", "name": "Laptop",   "price": 1200.00, "stock": 15},
#     {"id": "P002", "name": "Mouse",    "price": 25.50,   "stock": 40},

#Requirement 2: Data manipulation 
FILE_NAME = "inventory.json"
#help find product by its ID, returns the dictionary or none
def find_product(inventory, prodcut_id): 
    for product in inventory: 
        if product["id"].upper() == prodcut_id.upper():
            return product
    return None

def get_stock_input(prompt):
    stock = input(prompt)
    if not stock.isdigit():   #isdigit() also rejects negative numbers
        print("Invalid input. Please enter a whole number.")
        return None
    stock = int(stock)
    if stock > 500:
        print("Stock exceeds the maximum limit of 500.")
        return None
    return stock

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-"* 48)
    if not inventory:
        print("Inventory is empty.")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 48)

def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if product_id == "":
        print("Product ID cannot be empty.")
        return
    if find_product(inventory, product_id) is not None:
        print("Product ID already exists.")
        return

    name=input("Product Name: ").strip()

    #price can have decimals, so use float(),instead of a isdigit()
    try:
        price = float(input("Price: "))
    except ValueError:
        print("Invalid input. Price must be a number.")
        return
    if price < 0:
        print("Invalid input. Price cannot be negative.")
        return

    stock = get_stock_input("Stock Quantity: ")
    if stock is None:
        return

    inventory.append({"id": product_id, "name": name, "price": price, "stock": stock})
    print("\nProduct added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product Id:").strip()
    product = find_product(inventory, product_id)
    if product is None: 
        print("\nProduct not found.")
        return
    print("\nProduct Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    new_stock = get_stock_input("\nNew Stock Quantity: ")
    if new_stock is None:
        return
    product["stock"] = new_stock   #changes the dictionary inside the list directly
    print("\nStock updated successfully!")

def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = find_product(inventory, product_id)
    if product is None:
        print("\nProduct not found.")
        return
    print("\nProduct Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48) #prints "-" 48 times


#Requirement 3: Data Pesistence 
def load_inventory(): 
    if os.path.exists(FILE_NAME):
        print(f"{FILE_NAME} found.")
        with open(FILE_NAME, "r") as file: 
            inventory = json.load(file) #turns JSON text back into lists of dicts
        if inventory:   #only use the file if it actually has products in it
            print("Inventory loaded succesfully.")
            return inventory
        print(f"{FILE_NAME} is empty. Loading default products.")
    else:
        print(f"{FILE_NAME} not found. Loading default products.")

    #default products so option 1 always has something to show
    return [ {"id": "P001", "name": "Laptop",   "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse",    "price": 25.50,   "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00,   "stock": 25}
        ]

def save_inventory(inventory):
    with open(FILE_NAME, "w") as file: 
        json.dump(inventory, file, indent=4) #indent=4 makes the file readable 


#Requirement 4: Menu System
def show_menu(): 
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

def main():
    print("Inventory Management System")
    print()

    inventory = load_inventory()

    while True: 
        show_menu()
        option = input("\n Enter option: ").strip()
        if option == "1":
            display_all(inventory)
        elif option == "2":
            add_product(inventory)
        elif option == "3":
            update_stock(inventory)
        elif option == "4":
            search_product(inventory)
        elif option == "5":
            print("\nSaving inventory...")
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILE_NAME}.")
        elif option == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please enter 1-6.")


main()

   











  