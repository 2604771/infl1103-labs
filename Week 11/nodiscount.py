from discountstrategies import DiscountStrategy


class NoDiscount(DiscountStrategy):
    def apply(self, total:float)->float:
        return total