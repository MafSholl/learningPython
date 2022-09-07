
class Basket:
    def __init__(self):
        self.lst = [] * 3
        self.wallet = 10_000

    def add(self, item, price=0):
        if len(self.lst) < 3 and self.wallet-price >= 0:
            self.lst.append(item)
            self.wallet -= price
        else:
            if len(self.lst) >= 3:
                raise IndexError("Your basket is out of space joo")
            if self.wallet-price < 0:
                raise ValueError("Your money don finish! Abeg load ya wallet.")

    def find(self, item):
        for i in range(len(self.lst)):
            if self.lst[i] == item:
                return item
        return False

    # @dispatch (float, str)
    # def add(def v(elf, price, item):
    #     pass


