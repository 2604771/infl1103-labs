from product import Product
from supplier import Supplier


class DigitalProduct(Product): 
    def __init__(self,product_id:str,name:str,price:float,stock:int,download_size:float, supplier: Supplier):
        super().__init__(product_id,name,price,stock, supplier)
        self.__download_size = download_size

    def display_information(self)->None:
        super().display_information()
        print(f"Download size: {self.__download_size} MB")
        print(self.get_fulfilment_info())

    def get_fulfilment_info(self)->None:
        return "This product is delivered digitally via download"

    def to_dict(self)->None:
        data= super().to_dict()
        data["type"]= "digital"
        data["download size"] = self.__download_size
        return data
        

if __name__ == "__main__":
    Apple = Supplier("S001", "@Apple","sales@Apple.com")
    MacOs = DigitalProduct("P001", "MacOs", 299.99,10, 2.0, Apple)
    MacOs.display_information()
    print(MacOs.to_dict())
    





        