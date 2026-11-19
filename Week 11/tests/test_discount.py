from nodiscount import NoDiscount
from percentagediscount import PercentageDiscount
from bulkdiscount import BulkDiscount
from studentdiscount import StudentDiscount
from order import Order 
from supplier import Supplier
from productfactory import ProductFactory

def make_order_of_250(discount=None):
    apple = Supplier("S001", "Apple", "orders@apple.example")
    airpods = ProductFactory.create("physical", "P002", "AirPods", 50.00, 20, apple, weight=0.1)
    if discount is None:
        order = Order("O100")
    else:
        order = Order("O100", discount)
    order.add_order_line(airpods, 5)
    return order


def test_no_discount_returns_total_unchanged():
    discount = NoDiscount()
    assert discount.apply(250) == 250


def test_percentage_discount_takes_10_percent_off():
    discount = PercentageDiscount(10)
    assert discount.apply(250) == 225


def test_bulk_discount_applies_above_threshold():
    discount = BulkDiscount(200, 20)
    assert discount.apply(250) == 230


def test_bulk_discount_applies_at_exactly_threshold():
    discount = BulkDiscount(200, 20)
    assert discount.apply(200) == 180


def test_bulk_discount_not_applied_below_threshold():
    discount = BulkDiscount(200, 20)
    assert discount.apply(150) == 150


def test_student_discount_takes_5_percent_off():
    discount = StudentDiscount()
    assert discount.apply(250) == 237.5


def test_order_uses_no_discount_by_default():
    order = make_order_of_250()
    assert order.calculate_total() == 250


def test_order_total_uses_its_discount_strategy():
    order = make_order_of_250(BulkDiscount(200, 20))
    assert order.calculate_total() == 230


def test_set_discount_changes_strategy_on_existing_order():
    order = make_order_of_250(BulkDiscount(200, 20))
    order.set_discount(PercentageDiscount(10))
    assert order.calculate_total() == 225


def test_new_strategy_works_without_changing_order():
    order = make_order_of_250()
    order.set_discount(StudentDiscount())
    assert order.calculate_total() == 237.5
