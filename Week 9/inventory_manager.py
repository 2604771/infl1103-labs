import os
import json
from  product import Product
from inventory import Inventory


# Example of what the inventory list looks like:
# [
#     {"id": "P001", "name": "Laptop",   "price": 1200.00, "stock": 15},
#     {"id": "P002", "name": "Mouse",    "price": 25.50,   "stock": 40},

#Requirement 2: Data manipulation 
FILE_NAME = "inventory.json"

#Main Program (Get user input)
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

#Inventory class (Adds Prodcuts)
def add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if product_id == "":
        print("Product ID cannot be empty.")
        return
    if inventory.search_product(product_id) is not None:
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

    product = Product(product_id, name, price, stock)
    inventory.add_product(product)
    print("\nProduct added successfully!")

#Inventory Class (Update Stock)
def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product Id:").strip()
    product = inventory.search_product(product_id)
    if product is None: 
        print("\nProduct not found.")
        return
    print("\nProduct Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    new_stock = get_stock_input("\nNew Stock Quantity: ")
    if new_stock is None:
        return
    if product.update_stock(new_stock):
        print("\nStock updated successfully!")
    else:
        print("Invalid stock quantity. ")
#Inventory Class( Seach products)
def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)
    if product is None:
        print("\nProduct not found.")
        return
    print("\nProduct Found")
    print("-" * 48)
    product.display_information()
    print("-"*48)



#Requirement 3: Data Pesistence 
def load_inventory(): 

    inventory = Inventory()
    data = []
    if os.path.exists(FILE_NAME):
        print(f"{FILE_NAME} found.")
        with open(FILE_NAME, "r") as file: 
            data = json.load(file)

        if data: 
            print("Inventory loaded successfully.")
        else: 
            print(f"{FILE_NAME} is empty. Loading default products. ")
    else:
        print(f"{FILE_NAME} not found. Loading default products. ")
    
    if not data: 
        data = [ {"id": "P001", "name": "Laptop",   "price": 1200.00, "stock": 15},
        {"id": "P002", "name": "Mouse",    "price": 25.50,   "stock": 40},
        {"id": "P003", "name": "Keyboard", "price": 45.00,   "stock": 25}
        ]

    for item in data: 
        product = Product(item["id"], item["name"], item["price"], item["stock"])
        inventory.add_product(product)

    return inventory

#File handling class 
def save_inventory(inventory):
    data = []
    for product in inventory.get_products():     #"shelf, give me all your boxes"
        data.append(product.to_dict())           #"box, turn yourself into a dict"
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)          #save the list of dicts
       
#Main Program Class
def show_menu(): 
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

#Main Program Class
def main():
    print("Inventory Management System")
    print()

    inventory = load_inventory()

    while True: 
        show_menu()
        option = input("\n Enter option: ").strip()
        if option == "1":
            inventory.display_all()
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

   











  