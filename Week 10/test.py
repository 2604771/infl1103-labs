from DigitalProduct import DigitalProduct
from inventory import Inventory
from order import Order
from orderline import OrderLine
from PhysicalProduct import PhysicalProduct
from product import Product
from supplier import Supplier

#supplier Info: created on its own, before any product
apple = Supplier("S001", "Apple", "orders@apple.example")

#PhysicalProduct
macbook = PhysicalProduct("P001", "MacBook Air", 1000.00, 10, 2.0, apple)
#DigitalProduct
macos = DigitalProduct("D001", "macOS", 0.00, 100, 12000, apple)


#Test 2.2 Association:Supplier and Product
print("TEST 2.2: ASSOCIATION (Supplier and Product)")
print("=" * 48)

print("\n Supplier shown through each product ")
macbook.display_information()
macos.display_information()

#same supplier object, not two copies
print("\n Do both products share the same Supplier object? ")
print(macbook.get_supplier() is macos.get_supplier())
#two separate product objects
print("\n Are the two products the same object? ")
print(macbook is macos)

#Predict first: del only removes the variable name, not the Supplier object
print("\n After del apple: can the product still show its supplier? ")
del apple
macbook.display_information()


#Test 3 Aggregation: Inventory and Product
print("TEST 3: AGGREGATION (Inventory and Product)")

#aggregation: the product exists first, on its own,
# and then gets added to an inventory.
print("\n Inventory A after adding P001 ")
inventory_a = Inventory()
inventory_a.add_product(macbook)
inventory_a.display_all()

#3.remove it from A, then check the product still works
print("\n Remove P001 from Inventory A")
print(inventory_a.remove_product("P001"))

print("\nInventory A after removing P001")
inventory_a.display_all()

#Predict first: does the product still work after removal?
print("\nProduct after removal from Inventory A")
macbook.display_information()

#add the same product object to inventory B
print("\nInventory B after adding the same P001 ")
inventory_b =Inventory()
inventory_b.add_product(macbook)
inventory_b.display_all()

print("\nIs the product in Inventory B the same object? ")
print(inventory_b.find_product("P001") is macbook)

#Test 4
print("\n Test 4 ")
order1 = Order('001')
order1.add_order_line(macbook,2)
order1.add_order_line(macos,1 )

#Display each line and the total
print("\nOrder 1")
order1.display_order()

#add the same product ot a different order
order2= Order("002")
order2.add_order_line(macbook, 1)
print("\nOrder 2")
order2.display_order()

#Remove the orderlines 
line_in_order1 = order1.get_order_lines()[0]
line_in_order2 = order2.get_order_lines()[0]

print("\nAre the two OrderLines the same object?")
print(line_in_order1 is line_in_order2)

print("Do both OrderLines refer to the same Product object?")
print(line_in_order1.get_product() is line_in_order2.get_product())

#remove the order 
print("\nAfter del order1: does the product still exist?")
del order1
macbook.display_information()

print("\n Test 6.2:LSP")

def show_product_details(product: Product)->None:
        product.display_information()
        print(product.get_fulfilment_info())


#same function, given a PhysicalProduct
print("\nshow_product_details with a PhysicalProduct")
show_product_details(macbook)

#same function, given a DigitalProduct
print("\nshow_product_details with a DigitalProduct")
show_product_details(macos)

#both product types in ONE inventory, using its normal operations
print("\nBoth product types in one Inventory")
inventory = Inventory()
inventory.add_product(macbook)
inventory.add_product(macos)
inventory.display_all()

print("\n Test 7")
for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print()