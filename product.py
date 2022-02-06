class Product():
    def __init__(self, id, price, currency, quantity, matching_id, cd):
        self.id = int(id)
        self.price = int(price)
        self.currency = currency.strip()
        self.quantity = int(quantity)
        self.matching_id = int(matching_id)
        self.currenciesdict = cd
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        tp = self.price * self.quantity * float(self.currenciesdict['PLN']) * float(self.currenciesdict[self.currency])
        self.currency = 'PLN'
        return tp