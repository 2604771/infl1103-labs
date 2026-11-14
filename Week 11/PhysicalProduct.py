from CanBeShipped import CanBeShipped
from product import Product
from supplier import Supplier

Shipping_Base_Fee = 5.00
Shipping_Rate_Per_KG = 2.00

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self,product_id:str,name:str,price:float,stock: int,weight:float, supplier:Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self)->None:
        super().display_information()
        print(f"Weight: {self.__weight} kg | Shipping: ${self.calculate_shipping_cost():.2f}")
        
    
    def get_fulfilment_info(self)->str:
            return "This product requires physical shipping."

    def calculate_shipping_cost(self)->float:
         return Shipping_Base_Fee + self.__weight * Shipping_Rate_Per_KG

    def to_dict(self)->dict:
        data = super().to_dict() #parents build data
        data["type"] = "physical"
        data["weight"] = self.__weight #child extra attribute
        return data #return the finished dict
