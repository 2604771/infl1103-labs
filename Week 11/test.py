from bulkdiscount import BulkDiscount
from inventory import Inventory
from inventory_manager import get_positive_float, load_products
from order import Order
from percentagediscount import PercentageDiscount
from productfactory import ProductFactory
from studentdiscount import StudentDiscount
from supplier import Supplier

#supplier Info: created on its own, before any product
apple = Supplier("S001", "Apple", "orders@apple.example")

#PhysicalProduct
macbook = ProductFactory.create("physical", "P001", "MacBook Air", 1000.00, 10, apple, weight=2.0)
#DigitalProduct
macos = ProductFactory.create("digital", "D001", "macOS", 19.99, 100, apple, download_size=12000)

print("\n 3.2 Factory pattern ")
macbook.display_information()
print(macbook.to_dict())
macos.display_information()
print(macos.to_dict())

for weight in [0.5, 2.0, 10.0]:
    item = ProductFactory.create("physical", "T001", "Test box", 10.00, 1, apple, weight=weight)
    print(f"{weight} kg -> shipping ${item.calculate_shipping_cost():.2f}")

print("\n 2.3 Strategy pattern ")
desk = ProductFactory.create("physical", "P010", "Desk", 50.00, 20, apple, weight=10.0)
strategy_order = Order("O100", BulkDiscount(200, 20))
strategy_order.add_order_line(desk, 5)                 # 5 x 50 = 250
print("Bulk discount total:", strategy_order.calculate_total())

strategy_order.set_discount(PercentageDiscount(10))
print("Percentage discount total:", strategy_order.calculate_total())
print("\n 2.4 Extend without modifying ")
strategy_order.set_discount(StudentDiscount())
print("Student discount total:", strategy_order.calculate_total())


print("\n 4 Validation ")
try:
    ProductFactory.create("physical", "P004", "iPad", 0.00, 5, apple, weight=0.5)
except ValueError as error:
    print("Price 0 rejected:", error)

try:
    ProductFactory.create("digital", "D002", "iWork", 9.99, -1, apple, download_size=500)
except ValueError as error:
    print("Stock -1 rejected:", error)

try:
    strategy_order.add_order_line(macbook, 0)
except ValueError as error:
    print("Quantity 0 rejected:", error)


print("\n 5.1 User input (type: abc, then -5, then 12.50) ")
price = get_positive_float("Price: ")
print("Returned value:", price)


print("\n 5.2 Loading products from a file ")
csv_inventory = Inventory()
load_products("products.csv", csv_inventory, apple)
csv_inventory.display_all()

print("\n 5.2 Missing products file ")
load_products("missing_products.csv", Inventory(), apple)


print("\n 3.2 Unknown product type ")
ProductFactory.create("service", "S001", "AppleCare", 99.00, 5, apple)

