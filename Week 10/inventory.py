from product import Product

class Inventory:
    def __init__(self):
        #use base class product 
        self.__products:list[Product] = []  

    def add_product(self,product:Product) -> None:
        self.__products.append(product)

    def display_all(self) -> None :
        print ("\nCurrent Inventory")
        print ("-" *48)
        if not self.__products:
            print ("Inventory is empty.")
        for product in self.__products:
            product.display_information()
    
    def find_product(self, product_id: str ) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id.upper():
                return product
        return None

    def remove_product(self, product_id: str) -> bool:
        #call find_product method with parameter of product ID 
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def get_products(self) -> list[Product]:
        return self.__products
    















