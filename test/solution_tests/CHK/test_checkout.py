from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_checkout_individual(self):

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



