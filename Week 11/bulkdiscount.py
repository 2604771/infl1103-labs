from discountstrategies import DiscountStrategy


class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold:float, amount:float)->None:
        self.__threshold = threshold
        self.__amount = amount

    def apply(self, total:float)->float:
        if total >= self.__threshold:
            return total - self.__amount

        return total


if __name__ == "__main__":
    discount = BulkDiscount(200, 20)
    print(discount.apply(250))   
    print(discount.apply(200))   
    print(discount.apply(180))  