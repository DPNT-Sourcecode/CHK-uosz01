from solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():

    def test_checkout_individual(self):

        assert CheckoutSolution().checkout("") == 0
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15
        assert CheckoutSolution().checkout("E") == 40
        assert CheckoutSolution().checkout("F") == 10

        assert CheckoutSolution().checkout("G") == 20
        assert CheckoutSolution().checkout("H") == 10
        assert CheckoutSolution().checkout("I") == 35
        assert CheckoutSolution().checkout("J") == 60
        assert CheckoutSolution().checkout("K") == 70
        assert CheckoutSolution().checkout("L") == 90

        assert CheckoutSolution().checkout("M") == 15
        assert CheckoutSolution().checkout("N") == 40
        assert CheckoutSolution().checkout("O") == 10
        assert CheckoutSolution().checkout("P") == 50
        assert CheckoutSolution().checkout("Q") == 30
        assert CheckoutSolution().checkout("R") == 50

        assert CheckoutSolution().checkout("S") == 20
        assert CheckoutSolution().checkout("T") == 20
        assert CheckoutSolution().checkout("U") == 40
        assert CheckoutSolution().checkout("V") == 50
        assert CheckoutSolution().checkout("W") == 20
        assert CheckoutSolution().checkout("X") == 17

        assert CheckoutSolution().checkout("Y") == 20
        assert CheckoutSolution().checkout("Z") == 21


    def test_checkout_special(self):

        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("AAAAA") == 200
        assert CheckoutSolution().checkout("AAAAAA") == 250
        assert CheckoutSolution().checkout("AAAAAAA") == 300
        assert CheckoutSolution().checkout("AAAAAAAA") == 330

        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("EEB") == 80

        assert CheckoutSolution().checkout("FF") == 20
        assert CheckoutSolution().checkout("FFF") == 20
        assert CheckoutSolution().checkout("FFFF") == 30
        assert CheckoutSolution().checkout("FFFFF") == 40
        assert CheckoutSolution().checkout("FFFFFF") == 40

        assert CheckoutSolution().checkout("HHHHH") == 45
        assert CheckoutSolution().checkout("HHHHHH") == 55
        assert CheckoutSolution().checkout("HHHHHHH") == 65
        assert CheckoutSolution().checkout("HHHHHHHH") == 75
        assert CheckoutSolution().checkout("HHHHHHHHH") == 85
        assert CheckoutSolution().checkout("HHHHHHHHHH") == 80

        assert CheckoutSolution().checkout("KK") == 120

        assert CheckoutSolution().checkout("NNN") == 120
        assert CheckoutSolution().checkout("NNNM") == 120 + 0
        assert CheckoutSolution().checkout("NNNMM") == 120 + 15

        assert CheckoutSolution().checkout("PPPP") == 200
        assert CheckoutSolution().checkout("PPPPP") == 200

        assert CheckoutSolution().checkout("QQ") == 60
        assert CheckoutSolution().checkout("QQQ") == 80

        assert CheckoutSolution().checkout("RR") == 100
        assert CheckoutSolution().checkout("RRR") == 150
        assert CheckoutSolution().checkout("RRRQ") == 150 + 0
        assert CheckoutSolution().checkout("RRRQQ") == 150 + 0 + 30
        assert CheckoutSolution().checkout("RRRQQQ") == 150 + 0 + 60
        assert CheckoutSolution().checkout("RRRQQQQ") == 150 + 0 + 80

        assert CheckoutSolution().checkout("UU") == 80
        assert CheckoutSolution().checkout("UUU") == 120
        assert CheckoutSolution().checkout("UUUU") == 120 + 0
        assert CheckoutSolution().checkout("UUUUU") == 120 + 0 + 40
        assert CheckoutSolution().checkout("UUUUUU") == 120 + 0 + 80
        assert CheckoutSolution().checkout("UUUUUUU") == 120 + 0 + 120
        assert CheckoutSolution().checkout("UUUUUUUU") == 120 + 0 + 120 + 0

        assert CheckoutSolution().checkout("VV") == 90
        assert CheckoutSolution().checkout("VVV") == 130
        assert CheckoutSolution().checkout("VVVV") == 130 + 50
        assert CheckoutSolution().checkout("VVVVV") == 130 + 90
        assert CheckoutSolution().checkout("VVVVVV") == 130 + 130


    def test_checkout_group_offer(self):

        assert CheckoutSolution().checkout("ST") == 40
        assert CheckoutSolution().checkout("STZ") == 45



    def test_checkout_invalid(self):

        assert CheckoutSolution().checkout("z") == -1
        assert CheckoutSolution().checkout("%") == -1
        assert CheckoutSolution().checkout("AAg") == -1
        assert CheckoutSolution().checkout("a") == -1
        assert CheckoutSolution().checkout("ABCa") == -1


    def test_checkout_combination(self):

        assert CheckoutSolution().checkout("ABCD") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("DCBA") == 50 + 30 + 20 + 15
        assert CheckoutSolution().checkout("ABABACD") == 130 + 45 + 20 + 15

        assert CheckoutSolution().checkout("EEB") == 80
        assert CheckoutSolution().checkout("EEBB") == 80 + 30
        assert CheckoutSolution().checkout("EBB") == 40 + 45

        assert CheckoutSolution().checkout("FFAFBF") == 30 + 50 + 30
        assert CheckoutSolution().checkout("FFAFBFEEB") == 30 + 50 + 30 + 80

        assert CheckoutSolution().checkout("UUUVBVUUCVUV") == 120 + 0 + 80 + 130 + 50 + 30 + 20

        assert CheckoutSolution().checkout("RQQQRRQFQQFQF") == 150 + 0 + 80 + 80 + 20

        assert CheckoutSolution().checkout("KHHZHHKHJHH") == 65 + 21 + 120 + 60

        assert CheckoutSolution().checkout("SATZ") == 45 + 50






