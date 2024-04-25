from Rates import rates
import math

"""Dollar class"""

class Dollar:
    def __init__(self, amount):
        self.__amount = float(amount* rates['usd', 'nis'])
    def __str__(self):
        return f"{round(float(self.__amount* rates['nis', 'usd']), 2)} $"
    def __repr__(self):
        return f"Dollar({round(self.__amount * rates['nis', 'usd'], 2)})"
    def amount(self):
        return self.__amount
    def __add__(self, other):
        return Dollar(self.amount() + other.amount())
    def __sub__(self, other):
        return Dollar(self.amount() - other.amount())
    def convert(self, currency):
        if self.__class__.__name__ == 'Shekel':
            return self.amount()
        elif self.__class__.__name__ == 'Dollar':
            return self.amount() * rates['usd', 'nis']
        elif self.__class__.__name__ == 'Euro':
            return self.amount() * rates['eur', 'nis']