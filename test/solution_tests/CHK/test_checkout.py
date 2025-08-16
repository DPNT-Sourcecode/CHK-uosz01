from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_checkout_individual(self):

        assert CheckoutSolution().checkout("") == 0
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15

    def test_checkout_special(self):

        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("BB") == 45

    def test_checkout_invalid(self):

        assert CheckoutSolution().checkout("E") == -1
        assert CheckoutSolution().checkout("AAE") == -1
        assert CheckoutSolution().checkout("a") == -1
        assert CheckoutSolution().checkout("ABCa") == -1

    def test_checkout_combination(self):

        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DCBA") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("ABABACD") == 130 + 45 + 20 + 15



