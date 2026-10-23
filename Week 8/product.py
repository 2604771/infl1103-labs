#SRP: Product is responsible for representing and managing ONE product.
#It does not load/save files, ask for user input, or manage the whole inventory.

MAX_STOCK = 500

class Product:
    #from Week 5 line 66: {"id": product_id, "name": name, "price": price, "stock": stock}
    #each dict key becomes a private attribute
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    #getters: outside code can READ the values, but can't change them directly
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    #the product checks the value itself before accepting it (encapsulation)
    #returns True/False so the caller decides what message to show the user
    def update_stock(self, quantity):
        if quantity < 0 or quantity > MAX_STOCK:
            return False
        self.__stock = quantity
        return True

    #from Week 5 lines 36-37: the f-string that prints one product
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    #json can't save objects, so the product turns itself back into a dict for saving
    def to_dict(self):
        return {"id": self.__product_id, "name": self.__name,
                "price": self.__price, "stock": self.__stock}

