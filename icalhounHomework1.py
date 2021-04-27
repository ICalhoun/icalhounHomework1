from dataclasses import dataclass


@dataclass()
class PurchasedItem(object):
    name: str
    price: float
    type: str


def __get_tax_rate(state, items):
    tax_rates = {
        "ma": {
            "clothes": 0.0,
            "wic eligible food": 0.0,
            "everything else": 0.0625,
        },
        "nh": {
            "clothes": 0.0,
            "wic eligible food": 0.0,
            "everything else": 0.0,
        },
        "me": {
            "clothes": 0.055,
            "wic eligible food": 0.0,
            "everything else": 0.055,
        },
        "massachusetts": {
            "clothes": 0.0,
            "wic eligible food": 0.0,
            "everything else": 0.0625,
        },
        "new hampshire": {
            "clothes": 0.0635,
            "wic eligible food": 0.0,
            "everything else": 0.0635,
        },
        "maine": {
            "clothes": 0.055,
            "wic eligible food": 0.0,
            "everything else": 0.055,
        },
    }
    if (
        state.lower()[:2] == "ma"
        and items.type.lower() == "clothes"
        and items.price > 175
    ):
        return 0.0625
    else:
        return tax_rates[state.lower()][items.type.lower()]


def __get_price_with_tax(state, item):
    tax_rate = __get_tax_rate(state, item)
    if (
        state.lower()[:2] == "ma"
        and item.type.lower() == "clothes"
        and item.price > 175
    ):
        taxed_price = (tax_rate * (item.price - 175)) + item.price
    else:
        taxed_price = (tax_rate * item.price) + item.price
    return taxed_price


def calculate_total(state, customer_items):
    total = 0
    for items in customer_items:
        if items.price > 0.0:
            total = total + __get_price_with_tax(state, items)
    return round(total, 2)


if __name__ == "__main__":
    purchases = [PurchasedItem("test", 10.00, "clothes")]

    print("The total is: $" + str(calculate_total("MA", purchases)))
