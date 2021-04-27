from dataclasses import dataclass


@dataclass()
class PurchasedItem(object):
    name: str
    price: float
    type: str


def get_tax_rate(state, items):
    tax_rates = {'ma': {'clothes': .0625, 'wic eligible food': 0.0 ,'everything else': .0625},
                 'ct': {'clothes': .0635, 'wic eligible food': 0.0, 'everything else': .0635},
                 'me': {'clothes': .055, 'wic eligible food': 0.0, 'everything else': .055},
                 'massachusetts': {'clothes': .0625, 'wic eligible food': 0.0,'everything else': .0625},
                 'connecticut': {'clothes': .0635, 'wic eligible food': 0.0, 'everything else': .0635},
                 'maine': {'clothes': .055, 'wic eligible food': 0.0, 'everything else': .055}}
    return tax_rates[state.lower()][items.type.lower()]


def get_price_with_tax(state, item):
    tax_rate = get_tax_rate(state, item)
    taxed_price = (tax_rate * item.price) + item.price
    return taxed_price


def calculate_total(state, customer_items):
    total = 0
    for items in customer_items:
        if items.price > 0.0:
            total = total + get_price_with_tax(state, items)
    return round(total, 2)


if __name__ == "__main__":
    purchases = [PurchasedItem("test", 199.00, "clothes"),
                 PurchasedItem('test2', 10.00, 'everything else'),
                 PurchasedItem('test3', 10.00, 'everything else')]

    print(calculate_total('MA', purchases))
