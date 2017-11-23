#Object class which will hold's currency information
class currency:
    # Constructor
    def __init__(self, date, bank, buy, sell):
        self.date = date
        self.bank = bank
        self.buy = buy
        self.sell = sell

