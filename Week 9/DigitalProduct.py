from product import Product 

class DigitalProduct(Product): 
    def __init__(self,product_id,name,price,stock,download_size):
        super().__init__(product_id,name,price,stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} mb")

    def get_fulfilment_info(self):
        return "This product is delivered digitally via download"

    def to_dict(self):
        data= super().to_dict()
        data["type"]= "digital"
        data["download size"] = self.__download_size
        return data
        

    

if __name__ == "__main__":
    Laptop = DigitalProduct("P001", "Laptop", 299.99,10, 2.0)
    Laptop.display_information()
    print(Laptop.get_fulfilment_info())
    print(Laptop.to_dict())



        