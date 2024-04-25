from Euro import Euro
from Dollar import Dollar
from Shekel import Shekel

from Rates import rates

"""
main.py: main module
"""
def add(self, other_currency):

    return self.amount() + other_currency.amount()
def apply(operation, currency1, currency2):

    def add(currency1, currency2):
        amount = currency1.amount() + currency2.amount()
        if currency1.__class__.__name__ == 'Shekel':
            balance = Shekel(amount)
        elif currency1.__class__.__name__ == 'Dollar':
            balance = Dollar(amount * rates['nis', 'usd'])
        elif currency1.__class__.__name__ == 'Euro':
            balance = Euro(amount * rates['nis', 'eur'])
        return eval(balance.__repr__())

    def sub(currency1, currency2):
        amount  = currency1.amount() - currency2.amount()
        if currency1.__class__.__name__ == 'Shekel':
            balance = Shekel(amount)
        elif currency1.__class__.__name__ == 'Dollar':
            balance = Dollar(amount* rates['nis', 'usd'])
        elif currency1.__class__.__name__ == 'Euro':
            balance = Euro(amount* rates['nis', 'eur'])
        return balance.__repr__()

    operations = {'add': add, 'sub': sub}

    return operations[operation](currency1, currency2)
def convert(currency):
    if currency.__class__.__name__ == 'Shekel':
        print(currency.__repr__())
        return
    elif currency.__class__.__name__ == 'Dollar':
        temp = Shekel(currency.amount())
        print(temp.__repr__())
        return
    elif currency.__class__.__name__ == 'Euro':
        temp = Shekel(currency.amount)
        print(temp.__repr__())
        return
    else:
        raise ValueError(f"Unknown currency: {currency.__class__.__name__}")

coercions  = {
        ('nis', 'dollar'): lambda currency: convert(currency),
        ('nis', 'euro'): lambda currency: convert(currency),
        ('dollar', 'nis'): lambda currency: convert(currency),
        ('dollar', 'euro'): lambda currency: convert(currency),
        ('euro', 'nis'): lambda currency: convert(currency),
        ('euro', 'dollar'): lambda currency: convert(currency)
    }
def coerce_apply(operation , currency1, currency2):
    def add(currency1, currency2):
        amount =Shekel(currency1.amount() + currency2.amount())
        return amount.__repr__()

    def sub(currency1, currency2):
        amount =Shekel( currency1.amount() - currency2.amount())
        return amount.__repr__()

    operations = {'add': add, 'sub': sub}

    return operations[operation](currency1, currency2)


s = Shekel(50)
d = Dollar(50)
e = Euro(50)
print(d.amount())
print(e.amount())
print(d+s)
print(add(e, d))
z = eval(repr(d))
print(z)
print(s)
print(e)

print(d.amount())
print(s)


coercions[('dollar','nis')](Dollar(50))
print(coerce_apply('add', Shekel(50), Dollar(20)))
print(coerce_apply('add', Dollar(50), Euro(20)))
print(coerce_apply('sub', Dollar(50), Euro(20)))


