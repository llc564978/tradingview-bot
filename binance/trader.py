import ccxt

class BinanceTrader: 
    def __init__(self, apiKey, secret):
        self.exchange = ccxt.binance({
                            'apiKey': apiKey,
                            'secret': secret,
                            'options': {
                                'defaultType': 'future',  # or 'delivery' for COIN-M futures
                            },
                        })

    def getBalance(self):

        balance = self.exchange.fetch_balance()
        return balance
    
    def getMarket(self):

        market = self.exchange.load_markets()
        return market

    def trade(self, symbol, side, amount, takeProfitEp, stopLossEp):

        if side == 'buy':
            #order_info = self.exchange.create_market_buy_order(symbol=symbol, amount=amount)
            params = { 'stopPrice': 1700}
            sl = self.exchange.create_order(symbol=symbol, type='STOP_LOSS_LIMIT', side="sell", amount=amount, price=1700, params=params)
            tp = self.exchange.create_order(symbol=symbol, type='STOP_LOSS_LIMIT', side="sell", amount=amount, price=1700, params=params)
        elif side == "sell":
            #order_info = self.exchange.create_market_sell_order(symbol=symbol, amount=amount)
            sl = self.exchange.create_order(symbol=symbol, type='limit', side="buy", amount=amount, price=stopLossEp)
            tp = self.exchange.create_order(symbol=symbol, type='limit', side="buy", amount=amount, price=takeProfitEp)

        else:
            raise Exception("Error")


if __name__ == '__main__':


    binance = BinanceTrader("", "")
    print(binance.getBalance()['USDT'])
    binance.trade("BTC/USDT", "buy", 10, 1.0003, 1.0003)
    