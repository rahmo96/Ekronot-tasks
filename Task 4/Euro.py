from Rates import rates

"""Euro class"""
class Euro:
    def __init__(self, amount):
        self.__amount = amount* rates['eur' , 'nis']
    def __str__(self):
        return f"{self.__amount} €"
    def __repr__(self):
        return f"Euro({round(float(self.__amount)* rates['nis', 'eur'], 2)})"
    def amount(self):
        return self.__amount
    def __add__(self, other):
        return Euro(self.get_amount() + other.amount())
    def __sub__(self, other):
        return Euro(self.amount() - other.amount())

    def convert(self, currency):
        if self.__class__.__name__ == 'Shekel':
            return self.amount()
        elif self.__class__.__name__ == 'Dollar':
            return self.amount() * rates['usd', 'nis']
        elif self.__class__.__name__ == 'Euro':
            return self.amount() * rates['eur', 'nis']
