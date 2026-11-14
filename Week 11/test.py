from DigitalProduct import DigitalProduct
from inventory import Inventory
from order import Order
from PhysicalProduct import PhysicalProduct
from product import Product
from supplier import Supplier
from bulkdiscount import BulkDiscount
from percentagediscount import PercentageDiscount
from studentdiscount import StudentDiscount


    
#supplier Info: created on its own, before any product
apple = Supplier("S001", "Apple", "orders@apple.example")

#PhysicalProduct
macbook = PhysicalProduct("P001", "MacBook Air", 1000.00, 10, 2.0, apple)
#DigitalProduct
macos = DigitalProduct("D001", "macOS", 0.00, 100, 12000, apple)



print("\n 2.3 Strategy pattern ")
desk = PhysicalProduct("P010", "Desk", 50.00, 20, 10.0, apple)
strategy_order = Order("O100", BulkDiscount(200, 20))
strategy_order.add_order_line(desk, 5)                 # 5 x 50 = 250
print("Bulk discount total:", strategy_order.calculate_total())

strategy_order.set_discount(PercentageDiscount(10))
print("Percentage discount total:", strategy_order.calculate_total())
print("\n 2.4 Extend without modifying ")
strategy_order.set_discount(StudentDiscount())
print("Student discount total:", strategy_order.calculate_total())