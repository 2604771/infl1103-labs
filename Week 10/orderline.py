from product import Product

#OrderLine:one product + how many. It REFERS to a Product (association), it does not own it.
class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product:
        return self.__product

    #price is private in Product,so ask with the getter
    def calculate_subtotal(self) -> float:
        return self.__product.get_price() * self.__quantity

    def display_information(self) -> None:
        print(f"{self.__product.get_name()} x{self.__quantity} = ${self.calculate_subtotal():.2f}")