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
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAA") == 250
        assert CheckoutSolution().checkout("AAAAAAA") == 300
        assert CheckoutSolution().checkout("AAAAAAAA") == 330

        assert CheckoutSolution().checkout("BB") == 45

        assert CheckoutSolution().checkout("EEB") == 80

    def test_checkout_invalid(self):

        assert CheckoutSolution().checkout("H") == -1
        assert CheckoutSolution().checkout("%") == -1
        assert CheckoutSolution().checkout("AAG") == -1
        assert CheckoutSolution().checkout("a") == -1
        assert CheckoutSolution().checkout("ABCa") == -1

    def test_checkout_combination(self):

        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DCBA") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("ABABACD") == 130 + 45 + 20 + 15

        assert CheckoutSolution().checkout("EEB") == 80

        assert CheckoutSolution().checkout("EEBB") == 80 + 30
        assert CheckoutSolution().checkout("EBB") == 40 + 45


