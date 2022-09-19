import unittest
import hw1


class Hw1Test(unittest.TestCase):

    def testCash(self):

        portfolio = hw1.Portfolio()
        portfolio.add_cash(500)
        portfolio.withdraw_cash(400)
        self.assertEqual(portfolio.cash, 100)

    def testStock(self):

        portfolio = hw1.Portfolio()
        portfolio.add_cash(500)
        s = hw1.Stock("S1", 35)
        portfolio.buy_stock(s, 4)
        amount = portfolio.stocks["S1"]
        self.assertEqual(amount, 4)

    def testMutualFund(self):
        portfolio = hw1.Portfolio()
        portfolio.add_cash(500)
        m = hw1.MutualFund("M1")
        portfolio.buy_mutual_fund(m, 10)
        amount = portfolio.mutual_funds["M1"]
        self.assertEqual(amount, 10)


if __name__ == "__main__":
    unittest.main()