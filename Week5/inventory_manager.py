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

def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product Id:").strip()
    product = find_prodcut(inventory, product_id)
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


def main():
    
#Job A: Getting a validated input 
#def get_product_quantity(next_id): 
    product_name = input("Enter Product name (or 'quit' to exit): ")
    if product_name == 'quit':
        return 'quit'
    quantity = input("Enter Quantiy: ")
    if not quantity.isdigit():
            print("Invalid input. Please enter a valid integer.")
            return None
    quantity =int(quantity)
    
     #Ensure it is not a negative value 
    if quantity <0:  
        print ("Invalid Input.Inventory quantity ")  
        return None
    #Ensure it is not over-amount
    if quantity >500:
        print("Inventory quatity exceeds the maximum limit of 500.Please enter valid cound")
        return None
    
    cost = input("Enter Inventory Cost: ")
    if not cost.isdigit():
        print("Invalid input. Please enter a valid integer.")
        return None
    cost = int(cost)
    if cost < 0:
     print("Invalid input. Cost cannot be negative.")
     return None
    return (next_id, product_name, quantity, cost)

#to create a process delivery and tax amount modular 
#def process_delivery(current_total, new_value):
    return current_total+ new_value

#For tax amount on the cost
#def calculate_tax(amount):
    return amount *0.10

 #generated a report
#for generating report on total units processed and failed attempts
#def generate_report(total_units_processed, failed_attempts):
    print ("total unit proccessed:", total_units_processed)
    print ("total failed entried:", failed_attempts)
 
#Lab 4 Requirement 1: Start the program and read the information 
def load_inventory():
    print("load_inventory() has started running")
    #history arrays
    history= []
    if os.path.exists("inventory.txt"):
        print("inventory.txt found, attempting to open...")
        file = open ("inventory.txt", "r") #to open the file 
        lines = file.readlines()
        file.close()
        #to load the history and formatting it 
        for line in lines : 
            line = line.strip()
            if line == "":
             continue 
            parts = line.split(",")
            order_id = int(parts[0])
            name = parts[1]
            quantity = int(parts[2])
            cost = int(parts[3])
            history.append((order_id, name, quantity, cost)) 
            #history (0,1,2,3), "append" = addition to the list
    return history
def save_inventory(history):
    file = open("inventory.txt", "w")
    for order in history: 
        order_id, name, quantity, cost = order 
        file.write(f"{order_id},{name}, {quantity}, {cost}\n")
    file.close()

main()










  