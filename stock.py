class Stock:

    stockPrice = 0
    stockName = ''
    def __init__ (self):

        self.stockPrice = 250
        self.stockName = 'Apple'
    def getStockInfo (self):
        print (str(self.stockName ), ' Share Price : '
                + str(self.stockPrice ))
def crashStockMarket (self, price):
    self.stockPrice = price
    print ('Stock Market Crashed' )

obj = Stock()
obj.getStockInfo()
obj.crashStockMarket(200)
obj.getStockInfo()