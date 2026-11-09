from orderline import OrderLine
from product import Product


#It creates and owns its OrderLine parts (composition).
class Order:
    def __init__(self, order_id: str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    
    #gives back a COPY of the list, so outside code can look but can't add/remove lines itself
    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    #composition: the Order CREATES the OrderLine itself, it is never passed in
    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    #ask each OrderLine for its own subtotal and add them up
    def calculate_total(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total = total + line.calculate_subtotal()
        return total

    def display_order(self) -> None:
        print(f"\nOrder {self.__order_id}")
        for line in self.__order_lines:
            line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")