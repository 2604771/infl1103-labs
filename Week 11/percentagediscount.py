from discountstrategies import DiscountStrategy


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage:float)->None:
        self.__percentage=percentage

    def apply(self, total:float)->float:
        return total-(total *self.__percentage/100)


if __name__ == "__main__":
    discount = PercentageDiscount(10)
    print(discount.apply(250))