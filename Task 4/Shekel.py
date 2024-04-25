from Rates import rates


"""Shekel class"""
class Shekel:
    def __init__(self, amount):
        self.__amount = amount
    def __str__(self):
        return f"{self.__amount} ₪"
    def __repr__(self):
        return f"Shekel({round(self.amount() , 2)})"
    def amount(self):
        return self.__amount
    def __add__(self, currency):
        return self.amount() + currency.amount()
    def __sub__(self, currency):
        return self.amount() - currency.amount()

    def convert(self, currency):
        if currency.__class__.__name__ == 'Shekel':
            return self.amount()
        elif currency.__class__.__name__ == 'Dollar':
            return self.amount() * rates['usd', 'nis']
        elif currency.__class__.__name__== 'Euro':
            return self.amount() * rates['eur', 'nis']
