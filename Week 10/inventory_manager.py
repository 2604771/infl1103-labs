import json
import os

from DigitalProduct import DigitalProduct
from inventory import Inventory
from PhysicalProduct import PhysicalProduct
from supplier import Supplier

#Requirement 2: Data manipulation 
FILE_NAME = "inventory.json"
SUPPLIER = Supplier("S001", "Apple", "orders@apple.example")

#Main Program (Get user input)
def get_stock_input(prompt):
    while True:
        try:
            stock = int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if stock <0:
            print("Invalid input. Stock cannot be negative")
            continue
        if stock > 500:
         print("Stock exceeds the maximum limit of 500.")
         continue
        return stock

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue                      # skip the rest, ask again
        if value < 0:
            print("Invalid input. Value cannot be negative.")
            continue
        return value                      # valid → hand it back (also ends the loop)

#Inventory class (Adds Prodcuts)
def menu_add_product(inventory: Inventory):
    print("\nAdd New Product")
    product_id = input("Product ID: ").strip().upper()
    if product_id == "":
        print("Product ID cannot be empty.")
        return
    if inventory.find_product(product_id) is not None:
        print("Product ID already exists.")
        return

    name=input("Product Name: ").strip()

    #price can have decimals, so use float(),instead of a isdigit()
    price = get_positive_float("Price: ")

    stock = get_stock_input("Stock Quantity: ")

    product_type = input("Product Type (P = Physical, D = Digital): ").strip().upper()

    if product_type == "P":
       weight= get_positive_float("Weight(Kg):")
       product = PhysicalProduct (product_id, name, price, stock, weight, SUPPLIER)

    elif product_type == "D":
        download_size= get_positive_float("Download size(Mb):")
        product = DigitalProduct(product_id, name, price, stock, download_size, SUPPLIER)

    else:
        print("Invalid product type. Please enter P or D")
        return
    
    inventory.add_product(product)
    print("\nProduct added successfully!")

#Inventory Class (Update Stock)
def menu_update_stock(inventory: Inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product Id:").strip()
    product = inventory.find_product(product_id)
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

#Inventory Class(Seach products)
def menu_search_product(inventory: Inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = inventory.find_product(product_id)
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
    
    if not data: #adding existing products to inventory file
        data = [ {"id": "P001", "name": "Laptop",   "price": 1200.00, "stock": 15, "type": "physical" , "weight": 2.0 },
        {"id": "P002", "name": "Mouse",    "price": 25.50,   "stock": 15, "type": "physical" , "weight": 0.5,}, 
        {"id": "P003", "name": "window", "price": 45.00,   "stock": 15, "type" : "digital" , "download size" : 10}
        ]

    for item in data: 
        if item["type"] == "physical":
            product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item ["weight"], SUPPLIER)

        elif item["type"] == "digital":
            product= DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item ["download size"], SUPPLIER)

        inventory.add_product(product) #function in inventory class
        

      

    return inventory

#File handling class 
def save_inventory(inventory: Inventory):
    data = []
    for product in inventory.get_products():     
        data.append(product.to_dict())           
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)          
       
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
            inventory.display_all() #from inventory class
        elif option == "2":
            menu_add_product(inventory)
        elif option == "3":
            menu_update_stock(inventory)
        elif option == "4":
            menu_search_product(inventory)
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

   











  