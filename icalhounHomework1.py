from dataclasses import dataclass

@dataclass()
class item(object):
    name: str
    price: float
    type: str


def get_tax(state, items):
    if state == 'MA':
        if items.type == 'clothes':
            if items.price < 175.0:
                return 0
            else:
                return .0625
        elif items.type == 'Wic eligible food':
            return 0
        else:
            return .0625
    elif state == 'CT':
        if items.type == 'clothes':
            if items.price < 1000.00:
                return .0635
            else:
                return .0775
        elif items.type == 'Wic eligible food":':
            return 0
        else:
            return .0635
    else:
        if items.type == 'clothes':
            return .055
        elif items.type == 'WiC eligible food':
            return 0
        else:
            return .055


def get_price_with_tax(tax, price):
    calculated_tax = tax * price
    taxed_price = calculated_tax + price
    return taxed_price


def calculate_total(state, receipt):
    total = 0
    for items in receipt:
        tax = get_tax(state, items)
        if items.price > 0.0:
            total = total + get_price_with_tax(tax, items.price)
    return total


if __name__ == "__main__":
    receipt = [item("test", 199.00, "clothes"), item('test2', 10.00, 'other'), item('test3', 10.00, 'other')]
    print(calculate_total('MA', receipt))