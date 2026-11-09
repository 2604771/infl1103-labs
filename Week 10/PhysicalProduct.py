from CanBeShipped import CanBeShipped
from product import Product
from supplier import Supplier

Shipping_Base_Fee = 5.00
Shipping_Rate_Per_KG = 2.00

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self,product_id:str,name:str,price:float,stock: int,weight:float,supplier:Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self)->None:
        super().display_information()
        print(f"Weight: {self.__weight} kg | Shipping: ${self.calculate_shipping_cost():.2f}")
        print(self.get_fulfilment_info())
    
    def get_fulfilment_info(self):
            return "This product requires physical shipping."

    def calculate_shipping_cost(self):
         return Shipping_Base_Fee + self.__weight * Shipping_Rate_Per_KG

    def to_dict(self):
        data = super().to_dict() #parents build data
        data["type"] = "physical"
        data["weight"] = self.__weight #child extra attribute
        return data #return the finished dict
    

if __name__ == "__main__":
    Apple = Supplier("S001", "Apple", "sales@Apple.com")#Suppplier
    Macbook = PhysicalProduct("P001", "Macbook Air", 1000.00,10, 2.0,Apple)
    Macbook.display_information()
    print(f"Shipping cost: ${Macbook.calculate_shipping_cost():.2f}")
    print(Macbook.to_dict())
   
    
    for weight in [0.5, 2.0, 10.0]:
        item = PhysicalProduct("T001", "Test box", 10.00, 1, weight,Apple)
        print(f"{weight} kg -> shipping ${item.calculate_shipping_cost():.2f}")
        