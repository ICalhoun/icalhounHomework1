import icalhounHomework1
import pytest
from dataclasses import dataclass


@dataclass()
class PurchasedItem(object):
    name: str
    price: float
    type: str


def test_get_total_good_data():
    purchases = [
        PurchasedItem("test", 199.00, "everything else"),
        PurchasedItem("t-shirt", 24.00, "clothes"),
        PurchasedItem("apple", 0.50, "Wic Eligible Food"),
    ]
    total = icalhounHomework1.calculate_total("MA", purchases)
    assert total == 237.44
    total = icalhounHomework1.calculate_total("ME", purchases)
    assert total == 235.76
    total = icalhounHomework1.calculate_total("NH", purchases)
    assert total == 223.5


def test_get_total_price_is_not_float():
    purchases = [
        PurchasedItem("test", "199", "everything else"),
        PurchasedItem("t-shirt", 24.00, "clothes"),
        PurchasedItem("apple", 0.50, "Wic Eligible Food"),
    ]
    with pytest.raises(TypeError):
        total = icalhounHomework1.calculate_total("MA", purchases)
        assert total == 211.4375


def test_type_is_not_string():
    purchases = [
        PurchasedItem("test", 2.00, 1),
        PurchasedItem("t-shirt", 24.00, "clothes"),
        PurchasedItem("apple", 0.50, "Wic Eligible Food"),
    ]
    with pytest.raises(AttributeError):
        total = icalhounHomework1.calculate_total("MA", purchases)
        assert total == 2.125


def test_unsupported_state():
    good_purchase = [
        PurchasedItem("t-shirt", 24.00, "clothing"),
        PurchasedItem("t-shirt", 24.00, "clothes"),
        PurchasedItem("apple", 0.50, "Wic Eligible Food"),
    ]
    with pytest.raises(KeyError):
        total = icalhounHomework1.calculate_total("CA", good_purchase)
        assert total == 0


def test_negative_price():
    negative_purchase = [PurchasedItem("refund", -22.00, "wic eligible food")]
    total = icalhounHomework1.calculate_total("MA", negative_purchase)
    assert total == 0
