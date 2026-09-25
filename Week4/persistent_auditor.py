import os

def main():
    Total_Unit_Processed = 0
    Failed_entries = 0
    history = load_inventory()
    print("Current Orders:\n")

    for order in history: 
        order_id, name, quantity, cost = order
        print(f"{order_id}, {name}, {quantity}")
        print()
    if history: 
        next_id = history[-1][0] + 1
    else:
        next_id = 1001

    while True:
        result = get_product_quantity(next_id)  
        if result == 'quit':
            break

        if result is None:
            Failed_entries += 1
            continue

        order_id, name, quantity, cost = result
        history.append(result)
        Total_Unit_Processed += cost #still bundled together as one unit — 
        #not the four separate unpacked variables
        tax = calculate_tax(cost)
        print(f"\nNew Order Added:\n{order_id},{name},{quantity}\n")
        #"\n" still bundled together as one unit — not the four separate unpacked 
        #variables
        print(f"Tax on this order: {tax}")
        next_id += 1

    
    
    generate_report(Total_Unit_Processed , Failed_entries)

#Job A: Getting a validated input 
def get_product_quantity(next_id): 
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
def process_delivery(current_total, new_value):
    return current_total+ new_value

#For tax amount on the cost
def calculate_tax(amount):
    return amount *0.10

 #generated a report
#for generating report on total units processed and failed attempts
def generate_report(total_units_processed, failed_attempts):
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


main()










  