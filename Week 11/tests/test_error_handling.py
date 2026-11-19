from inventory_manager import get_positive_float, load_products
from inventory import Inventory
from supplier import Supplier

apple = Supplier("S001", "Apple", "Order@apple.com")

def test_get_positive_float_asks_again_until_valid(monkeypatch, capsys):
    answers = iter(["abc", "-5", "12.50"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    value = get_positive_float("Price: ")

    printed = capsys.readouterr().out
    assert value == 12.5
    assert "Please enter a valid number, e.g. 12.50" in printed
    assert "Please enter a number greater than zero." in printed


def test_get_positive_float_rejects_zero(monkeypatch, capsys):
    answers = iter(["0", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    value = get_positive_float("Price: ")

    assert value == 5.0
    assert "Please enter a number greater than zero." in capsys.readouterr().out


def test_load_products_skips_bad_rows_and_loads_valid_ones(tmp_path, capsys):
    csv_file = tmp_path / "products.csv"
    csv_file.write_text(
        "product_type,product_id,name,price,stock_quantity\n"
        "physical,P001,MacBook Air,1000.00,10\n"
        "digital,D001,macOS,19.99,100\n"
        "service,S001,AppleCare,99.00,5\n"
        "physical,P002,iPad,abc,3\n"
        "physical,P003,iPhone,799.00,7\n"
    )
    inventory = Inventory()

    load_products(str(csv_file), inventory, apple)

    printed = capsys.readouterr().out
    assert len(inventory.get_products()) == 3
    assert inventory.find_product("P001") is not None
    assert inventory.find_product("S001") is None
    assert inventory.find_product("P002") is None
    assert "Unknown product type: service" in printed
    assert "3 products loaded." in printed
    assert "Load attempt finished." in printed


def test_load_products_handles_missing_file(tmp_path, capsys):
    missing = tmp_path / "does_not_exist.csv"
    inventory = Inventory()

    load_products(str(missing), inventory, apple)

    printed = capsys.readouterr().out
    assert len(inventory.get_products()) == 0
    assert "Products file not found" in printed
    assert "Load attempt finished." in printed
    assert "products loaded" not in printed