#SRP: Inventory is responsible for managing a collection of Product objects.
from product import Product

class Inventory:
    def __init__(self):
        self.__products = []    #private list, starts empty

    def add_product(self, product):
        self.__products.append(product)

    def display_all(self):
        print ("\nCurrent Inventory")
        print ("-" *48)
        if not self.__products:
            print ("Inventory is empty.")
        for product in self.__products:
            product.display_information()
        print("_"*48)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id.upper():
                return product
        return None

    def get_product(self):
        return self.__products
    
if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
    inventory.add_product(Product("P002", "Mouse", 25.50, 40))
    inventory.display_all()
    found = inventory.search_product("p002")    #lowercase on purpose
    if found:
        found.display_information()             #should show Mouse
    print(inventory.search_product("P999"))     #should print None














