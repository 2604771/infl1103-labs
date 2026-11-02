from product import Product 

class DigitalProduct(Product): 
    def __init__(self,product_id,name,price,stock,download_size):
        super().__init__(product_id,name,price,stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.__download_size} mb")

if __name__ == "__main__":
    Laptop = DigitalProduct("P001", "Laptop", 299.99,10, 2.0)
    Laptop.display_information()


        