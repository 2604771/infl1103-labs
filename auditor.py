inventory = 0 
failed_entries = 0
Total_Unit_Processed = 0
#Requirement 2: Continuous Loop for user to enter stock quantity until
#the user types quit
while True:
    inventory = input("Enter the inventory count (or 'quit' to exit): ")
    # Check quit first
    if inventory == 'quit':
        break
    #Requirement 4: Handle invalid input if enter is strings
    if not inventory.isdigit():
        print("Invalid input. Please enter a valid integer.")
        failed_entries += 1
        continue
    #Requirement 3: Accept stock values as integers 
    inventory = int(inventory)
    #Requirement 5: Business rules to reject negative numbers 
    if inventory < 0:
        print("Invalid input. Inventory count cannot be negative.")
        failed_entries += 1
        continue
    #Requirement 6: Manage state of a running total of the inventory
    Total_Unit_Processed += inventory
    #Requirement 7: Triger Overstock alert of 500 units 
    if inventory >500:
        print("Inventory count exceeds the maximum limit of 500. Please enter a valid count.")
        failed_entries += 1
        continue
#Requirement 8: Create a report of the total units processed and the number of failed entries
print("total units processed:", Total_Unit_Processed)
print("total failed entries:", failed_entries)






  