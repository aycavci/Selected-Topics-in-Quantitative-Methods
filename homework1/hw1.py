import random
from datetime import datetime

available_stocks = []


class MutualFund:
    def __init__(self, name):
        self.name = name
        self.price = 1


class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        available_stocks.append(self)


class History:
    def __init__(self, category, action, amount, name=None, price=None, date=datetime.now()):
        self.category = category
        self.action = action
        self.amount = amount
        self.name = name
        self.price = price
        self.date = date


class Portfolio:
    mutual_funds = {}
    stocks = {}
    cash = 0
    histories = []

    def add_cash(self, money):
        self.cash += money
        history = History("Cash", "Add", money)
        self.histories.append(history)

    def withdraw_cash(self, money):
        self.cash -= money
        history = History("Cash", "Withdraw", money)
        self.histories.append(history)

    def buy_stock(self, stock, amount):
        name = stock.name
        price = stock.price
        if stock in available_stocks:
            if self.cash >= price*amount:
                self.cash -= price*amount
                self.stocks[name] = amount
                history = History("Stock", "Buy", amount, name, price)
                self.histories.append(history)
            else:
                print("There is no such available stock or you do not have enough cash")

    def sell_stock(self, name, amount):
        if name in self.stocks.keys():
            stock_amount = self.stocks[name]
            if amount <= stock_amount:
                stock_amount -= amount
                for available_stock in available_stocks:
                    if name == available_stock.name:
                        price = available_stock.price
                        uniform_price = random.uniform(0.5*price, 1.5*price)
                        total_price = uniform_price * amount
                        self.cash += total_price
                        history = History("Stock", "Sell", amount, name, uniform_price)
                        self.histories.append(history)
            else:
                print("The amount you have is less than that you want to sell")
        else:
            print("There is no such stock available in your stocks")

    def buy_mutual_fund(self, mutual_fund, amount):
        name = mutual_fund.name
        price = mutual_fund.price
        if self.cash >= price * amount:
            self.cash -= price * amount
            self.mutual_funds[name] = amount
            history = History("Mutual Fund", "Buy", amount, name, price)
            self.histories.append(history)
        else:
            print("You do not enough cash")

    def sell_mutual_fund(self, name, amount):
        if name in self.mutual_funds.keys():
            mutual_fund_amount = self.mutual_funds[name]
            if amount <= mutual_fund_amount:
                mutual_fund_amount -= amount
                price = self.mutual_funds[name]
                uniform_price = random.uniform(0.9 * price, 1.2 * price)
                total_price = uniform_price * amount
                self.cash += total_price
                history = History("Mutual Fund", "Sell", amount, name, uniform_price)
                self.histories.append(history)
            else:
                print("The amount you have is less than that you want to sell")
        else:
            print("There is no such mutual fund available in your mutual funds")

    def __str__(self):
        cash = self.cash
        print("PORTFOLIO")
        print("----------------------------------------------")
        print("Cash: $" + str(cash))
        print("Stocks: ")
        stocks = self.stocks.keys()
        for stock in stocks:
            print(stock + "   " + str(self.stocks[stock]))
        print("Mutual Funds: ")
        mutual_funds = self.mutual_funds.keys()
        for mutual_fund in mutual_funds:
            print(mutual_fund + "   " + str(self.mutual_funds[mutual_fund]))
        return ''

    def history(self):
        self.histories.reverse()
        print("HISTORY")
        print("-----------------------------------------------")
        for history in self.histories:
            print("Date: " + str(history.date) + " | " + "Category: " + str(history.category) + " | " + "Action : " +
                  str(history.action) + " | " + "Amount: " + str(history.amount) + " | " + "Name: " + str(history.name)
                  + " | " + "Price: " + str(history.price))


# portfolio = Portfolio()
# portfolio.add_cash(600.8)
# s = Stock("S1", 40)
# portfolio.buy_stock(s, 6)
# mf1 = MutualFund("M1")
# mf2 = MutualFund("M2")
# portfolio.buy_mutual_fund(mf1, 9.8)
# portfolio.buy_mutual_fund(mf2, 7)
# print(portfolio)
# portfolio.sell_mutual_fund("M1", 5)
# portfolio.sell_stock("S1", 2)
# portfolio.withdraw_cash(100)
# portfolio.history()










