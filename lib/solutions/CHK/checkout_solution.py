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
        
        # Turn to upper case and count occurrence of each item
        skus = skus.upper()
        all_items_freq = Counter(skus)

        # Check for any invalid items and return -1
        if any(x not in self.prices.keys() for x in all_items_freq.keys()):
            return -1

        # Loop over all offers available
        for item in self.offers.keys():

            # Variables for readability
            item_freq = all_items_freq[item]
            offer_freq = (self.offers[item])[0]

            # If there are enough items to apply an offer
            if item_freq >= offer_freq:

                num_offers = item_freq // offer_freq
                all_items_freq[item] = item_freq % offer_freq


        items_cost = {k: all_items_freq[k] * self.prices[k] for k in all_items_freq.keys()}
        total = sum(items_cost.values())

        return total
        












