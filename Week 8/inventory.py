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
    

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id.upper():
                return product
        return None

    def get_products(self):
        return self.__products
    















