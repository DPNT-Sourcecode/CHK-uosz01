from collections import Counter

class CheckoutSolution:

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    offers = {
        "A": (3, 130),
        "B": (2, 45)
    }    

    # skus = unicode string
    def checkout(self, skus):
        
        skus = skus.upper()
        item_freq = Counter(skus)

        print((self.prices.keys()))

        if any(x not in item_freq.keys() for x in self.prices.keys()):
            return -1

        # total = 






