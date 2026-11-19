import pytest

from productfactory import ProductFactory
from order import Order
from supplier import Supplier


apple = Supplier("S001", "Apple", "orders@apple.example")


def test_price_of_zero_is_rejected():
    with pytest.raises(ValueError, match="Price must be greater than zero"):
        ProductFactory.create("physical", "P004", "iPad", 0.00, 5, apple, weight=0.5)


def test_negative_price_is_rejected():
    with pytest.raises(ValueError, match="Price must be greater than zero"):
        ProductFactory.create("physical", "P004", "iPad", -10.00, 5, apple, weight=0.5)


def test_negative_stock_is_rejected():
    with pytest.raises(ValueError, match="Stock quantity cannot be negative"):
        ProductFactory.create("digital", "D002", "iWork", 9.99, -1, apple, download_size=500)


def test_zero_stock_is_allowed():
    product = ProductFactory.create("digital", "D002", "iWork", 9.99, 0, apple, download_size=500)
    assert product.get_stock() == 0


def test_order_quantity_of_zero_is_rejected():
    macbook = ProductFactory.create("physical", "P001", "MacBook Air", 1000.00, 10, apple, weight=2.0)
    order = Order("O100")
    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        order.add_order_line(macbook, 0)


def test_negative_order_quantity_is_rejected():
    macbook = ProductFactory.create("physical", "P001", "MacBook Air", 1000.00, 10, apple, weight=2.0)
    order = Order("O100")
    with pytest.raises(ValueError, match="Quantity must be greater than zero"):
        order.add_order_line(macbook, -3)