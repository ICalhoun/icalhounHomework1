import icalhounHomework1
import pytest
from dataclasses import dataclass


@dataclass()
class PurchasedItem(object):
    name: str
    price: float
    type: str


def test_get_tax_rate_good_data_massachusetts():
    purchases = [PurchasedItem("test", 199.00, "everything else"),
                 PurchasedItem('t-shirt', 24.00, 'clothes'),
                 PurchasedItem('apple', 0.50, 'Wic Eligible Food')]
    tax_rate = icalhounHomework1.get_tax_rate('ma', purchases[0])
    assert tax_rate == 0.0625
    tax_rate = icalhounHomework1.get_tax_rate('massachusetts', purchases[1])
    assert tax_rate == 0.0625
    tax_rate = icalhounHomework1.get_tax_rate('MA', purchases[2])
    assert tax_rate == 0.0


def test_get_tax_rate_good_data_maine():
    purchases = [PurchasedItem("test", 199.00, "everything else"),
                 PurchasedItem('t-shirt', 24.00, 'clothes'),
                 PurchasedItem('apple', 0.50, 'Wic Eligible Food')]
    tax_rate = icalhounHomework1.get_tax_rate('me', purchases[0])
    assert tax_rate == 0.055
    tax_rate = icalhounHomework1.get_tax_rate('maine', purchases[1])
    assert tax_rate == 0.055
    tax_rate = icalhounHomework1.get_tax_rate('ME', purchases[2])
    assert tax_rate == 0.0


def test_get_tax_rate_good_data_connecticut():
    purchases = [PurchasedItem("test", 199.00, "everything else"),
                 PurchasedItem('t-shirt', 24.00, 'clothes'),
                 PurchasedItem('apple', 0.50, 'Wic Eligible Food')]
    tax_rate = icalhounHomework1.get_tax_rate('ct', purchases[0])
    assert tax_rate == 0.0635
    tax_rate = icalhounHomework1.get_tax_rate('connecticut', purchases[1])
    assert tax_rate == 0.0635
    tax_rate = icalhounHomework1.get_tax_rate('CT', purchases[2])
    assert tax_rate == 0.0


def test_get_tax_rate_bad_data_ma():
    purchases = [PurchasedItem('test', 199.00, 'everything else')]
    with pytest.raises(KeyError):
        tax_rate = icalhounHomework1.get_tax_rate('CA', purchases)


def test_get_price_with_tax_good_data():
    purchases = [PurchasedItem("test", 199.00, "everything else")]
    price_with_tax = icalhounHomework1.get_price_with_tax('MA', purchases[0])
    assert price_with_tax == 211.4375
    price_with_tax = icalhounHomework1.get_price_with_tax('ME', purchases[0])
    assert price_with_tax == 209.945
    price_with_tax = icalhounHomework1.get_price_with_tax('CT', purchases[0])
    assert price_with_tax == 211.6365


def test_get_price_with_tax_bad_data():
    purchases = [PurchasedItem('test', '199', 'clothes'),
                 PurchasedItem('apple', 3.0, 'none')]
    with pytest.raises(TypeError):
        price_with_tax = icalhounHomework1.get_price_with_tax('MA', purchases[0])
    with pytest.raises(KeyError):
        price_with_tax = icalhounHomework1.get_price_with_tax('MA', purchases[1])


def test_get_total_good_data():
    purchases = [PurchasedItem("test", 199.00, "everything else"),
                 PurchasedItem('t-shirt', 24.00, 'clothes'),
                 PurchasedItem('apple', 0.50, 'Wic Eligible Food')]
    total = icalhounHomework1.calculate_total('MA', purchases)
    assert total == 237.44
    total = icalhounHomework1.calculate_total('ME', purchases)
    assert total == 235.76
    total = icalhounHomework1.calculate_total('CT', purchases)
    assert total == 237.66


def test_get_total_bad_data():
    purchases = [PurchasedItem("test", '199', "everything else")]
    purchases2 = [PurchasedItem('test', 2.00, 1)]
    with pytest.raises(TypeError):
        total = icalhounHomework1.calculate_total('MA', purchases)
    with pytest.raises(AttributeError):
        total = icalhounHomework1.calculate_total('MA', purchases2)
