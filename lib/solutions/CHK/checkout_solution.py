from collections import Counter

def make_offer_dict(offer_item, num_offer_item, reward_item, num_reward_item, reward_offer_price):

    offer_dict = {
        "offer_item": offer_item,
        "num_offer_item": num_offer_item,
        "reward_item": reward_item,
        "num_reward_item": num_reward_item,
        "reward_offer_price": reward_offer_price
    }

    return offer_dict

class CheckoutSolution:

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,

        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,

        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,

        "Y": 10,
        "Z": 50
    }

    offers = [
        make_offer_dict("A", 5, "A", 5, 200),
        make_offer_dict("A", 3, "A", 3, 130),

        make_offer_dict("E", 2, "B", 1, 0),
        make_offer_dict("B", 2, "B", 2, 45),

        make_offer_dict("F", 3, "F", 1, 0),

        make_offer_dict("H", 10, "H", 10, 80),
        make_offer_dict("H", 5, "H", 5, 45),

        make_offer_dict("K", 2, "K", 2, 150),

        make_offer_dict("N", 3, "M", 1, 0),

        make_offer_dict("P", 5, "P", 5, 200),

        make_offer_dict("R", 3, "Q", 1, 0),
        make_offer_dict("Q", 3, "Q", 3, 80),

        make_offer_dict("U", 4, "U", 1, 0),

        make_offer_dict("V", 3, "V", 3, 130),
        make_offer_dict("V", 2, "V", 2, 90),
    ] 

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
        for offer in self.offers:

            # What item does the offer apply and how many
            offer_item = offer["offer_item"]
            num_offer_item = offer["num_offer_item"]

            # What item does the offer reward, how many, and offer price
            reward_item = offer["reward_item"]
            num_reward_item = offer["num_reward_item"]
            reward_offer_price = offer["reward_offer_price"]

            # How many of the offer items and reward items do we have
            offer_item_freq = all_items_freq[offer_item]
            reward_item_freq = all_items_freq[reward_item]

            # If there are enough items to apply an offer
            if offer_item_freq >= num_offer_item:

                # Calculate how many offers are available
                num_offers_available = offer_item_freq // num_offer_item

                # Calculate how many times the offer can be used on reward item
                num_offers_possible = reward_item_freq // num_reward_item

                # Find the number of offers that can be applied to the total
                num_offers_used = min(num_offers_available, num_offers_possible)

                # Subtract the offer reward items off the main count
                all_items_freq[reward_item] -= num_offers_used * num_reward_item

                # Ensure it doesn't drop below 0
                all_items_freq[reward_item] = max(all_items_freq[reward_item], 0)

                # Add offer price to the running total
                total += num_offers_used * reward_offer_price

        # Multiply the frequency of each item by its price
        items_cost = {k: all_items_freq[k] * self.prices[k] for k in all_items_freq.keys()}

        # Add to total
        total += sum(items_cost.values())

        return total
        







