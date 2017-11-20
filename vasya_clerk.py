"""
Solution for "Vasya - Clerk" kata:
https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
"""
TWENTY_FIVE = 25
FIFTY = 50
ONE_HUNDRED = 100
ALLOWED_SLOTS = [TWENTY_FIVE, FIFTY, ONE_HUNDRED]

POSITIVE = 'YES'
NEGATIVE = 'NO'

PRICE = TWENTY_FIVE


class Wallet(object):
    moneys = {}

    def __init__(self):
        super(Wallet, self).__init__()
        self.moneys = {
            TWENTY_FIVE: 0,
            FIFTY: 0,
            ONE_HUNDRED: 0
        }

    def is_supported_bill(self, money):
        if money not in ALLOWED_SLOTS:
            raise RuntimeError(u'Unsupported bill')

    def add_money(self, money):
        self.is_supported_bill(money)
        self.moneys[money] += 1

    def remove_money(self, money, amount=1):
        self.is_supported_bill(money)
        if not self.check_money(money, amount):
            raise RuntimeError(u'Not enough funds')
        self.moneys[money] -= amount

    def check_money(self, money, amount=1):
        self.is_supported_bill(money)
        return self.moneys[money] >= amount

    def calculate_exchange(self, money):
        self.is_supported_bill(money)

        if money == FIFTY:
            if self.check_money(TWENTY_FIVE):
                self.add_money(money)
                self.remove_money(TWENTY_FIVE)
            else:
                return False

        if money == ONE_HUNDRED:
            # if no 25 exists
            if self.check_money(TWENTY_FIVE):
                # try to get exchange with 50 + 25
                if self.check_money(FIFTY):
                    self.add_money(money)
                    self.remove_money(FIFTY)
                    self.remove_money(TWENTY_FIVE)
                elif self.check_money(TWENTY_FIVE, 3):
                    self.add_money(money)
                    self.remove_money(TWENTY_FIVE, 3)
                else:
                    return False
            else:
                return False

        return True


def tickets(people):
    wallet = Wallet()

    for idx, p in enumerate(people):
        # if first people
        if not idx:
            if p == PRICE:
                wallet.add_money(PRICE)
            else:
                return NEGATIVE
        else:
            if p == PRICE:
                wallet.add_money(PRICE)
            else:
                if not wallet.calculate_exchange(p):
                    return NEGATIVE
    return POSITIVE
