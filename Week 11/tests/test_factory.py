import pytest 
import pytest

from productfactory import ProductFactory
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from product import Product
from supplier import Supplier


apple = Supplier("S001", "Apple", "orders@apple.example")


def test_factory_creates_physical_product():
    product = ProductFactory.create("physical", "P001", "MacBook Air", 1000.00, 10, apple, weight=2.0)
    assert isinstance(product, PhysicalProduct)
    assert product.get_name() == "MacBook Air"


def test_factory_creates_digital_product():
    product = ProductFactory.create("digital", "D001", "macOS", 19.99, 100, apple, download_size=12000)
    assert isinstance(product, DigitalProduct)
    assert product.get_price() == 19.99


def test_factory_returns_a_product():
    product = ProductFactory.create("physical", "P001", "MacBook Air", 1000.00, 10, apple, weight=2.0)
    assert isinstance(product, Product)


def test_factory_passes_weight_to_physical_product():
    product = ProductFactory.create("physical", "P001", "MacBook Air", 1000.00, 10, apple, weight=2.0)
    assert product.calculate_shipping_cost() == 9.00


def test_unknown_product_type_raises_value_error():
    with pytest.raises(ValueError, match="Unknown product type: service"):
        ProductFactory.create("service", "S001", "AppleCare", 99.00, 5, apple)