from product import Product
from CanBeShipped import CanBeShipped

Shipping_Base_Fee = 5.00
Shipping_Rate_Per_KG = 2.00

class PhysicalProduct(Product):
    def __init__(self,product_id,name,price,stock,weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
            return "This product requires physical shipping."

    def calculate_shipping_cost(self):
         return Shipping_Base_Fee + self.__weight * Shipping_Rate_Per_KG
    
    

if __name__ == "__main__":
    Laptop = PhysicalProduct("P001", "Laptop", 299.99,10, 2.0)
    Laptop.display_information()
    print(Laptop.get_fulfilment_info())
    print(f"Shipping cost: ${Laptop.calculate_shipping_cost():.2f}")