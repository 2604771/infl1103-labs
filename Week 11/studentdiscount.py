from discountstrategies import DiscountStrategy


class StudentDiscount(DiscountStrategy):

    def apply(self,total:float)->float:
        return total-(total*5/100)
