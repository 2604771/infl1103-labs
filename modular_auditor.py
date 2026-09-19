





#Requirement 2: Create a get valid input function to accept the inventory key in
#Job A: Getting a validated input 
#Job B: Keeping running totals (Total_Unit_Processed,failed entries)
def get_valid_input(): 
    entry = input ("Enter the inventory the inventory count (or 'quit' to exit ):")
    if entry =='quit':
        return 'quit'
    #Ensure it is an integer inserted
    if not entry.isdigit():
        print("Invalid input. Please enter a valid integer.")
        return None
    entry =int(entry)
    #Ensure it is not a negative value 
    if entry <0:  
        print ("Invalid Input.Inventory count ")  
        return None
    #Ensure it is not over-amount
    if entry >500:
        print("Inventory count exceeds the maximum limit of 500.Please enter valid cound")
        return None

    return entry

#to create a process delivery and tax amount modular 
def process_delivery(current_total, new_value):
    return current_total+ new_value

def calculate_tax(amount):
    return amount *0.10

 #generated a report
def generate_report(total_units_processed, failed_attempts):
    print ("total unit proccessed:", total_units_processed)
    print ("total failed entried:", failed_attempts)










  