inventory = 0 
failed_entries = 0
Total_Unit_Processed = 0
while True:
    inventory = input("Enter the inventory count (or 'quit' to exit): ")
    # Check quit first
    if inventory == 'quit':
        break 
    inventory = int(inventory)
    if not inventory.isdigit():
        print("Invalid input. Please enter a valid integer.")
        failed_entries += 1
        continue
    if inventory < 0:
        print("Invalid input. Inventory count cannot be negative.")
        failed_entries += 1
        continue
    Total_Unit_Processed += inventory






  