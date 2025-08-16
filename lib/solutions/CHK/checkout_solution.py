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
        all_items_freq = Counter(skus)

        if any(x not in self.prices.keys() for x in all_items_freq.keys()):
            return -1

        for item in self.offers.keys():

            item_num = 

            if all_items_freq[item] >= (self.offers[item])[0]:

                num_offers = all_items_freq[item] // (self.offers[item])[0]
                all_items_freq[item] = all_items_freq[item] % (self.offers[item])[0]


        items_cost = {k: all_items_freq[k] * self.prices[k] for k in all_items_freq.keys()}
        total = sum(items_cost.values())

        return total
        











