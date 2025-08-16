from collections import Counter

class CheckoutSolution:

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    }

    offers = {
        "A": (3, 130),
        "B": (2, 45)
    }    

    # skus = unicode string
    def checkout(self, skus):

        if not(skus.isupper()) and skus != "":
            return -1
        
        # Count occurrence of each item
        all_items_freq = Counter(skus)

        # Check for any invalid items and return -1
        if any(x not in self.prices.keys() for x in all_items_freq.keys()):
            return -1

        total = 0

        # Loop over all offers available
        for item in self.offers.keys():

            # Variables for readability
            item_freq = all_items_freq[item]
            offer_freq = (self.offers[item])[0]
            offer_val = (self.offers[item])[1]

            # If there are enough items to apply an offer
            if item_freq >= offer_freq:

                # Calculate how many times the offer can be used
                num_offers = item_freq // offer_freq

                # Subtract the offer items off the main count
                all_items_freq[item] = item_freq % offer_freq

                # Add offer price to the running total
                total += num_offers * offer_val

        # Multiply the frequency of each item by its price
        items_cost = {k: all_items_freq[k] * self.prices[k] for k in all_items_freq.keys()}

        # Add to total
        total += sum(items_cost.values())

        return total
        










