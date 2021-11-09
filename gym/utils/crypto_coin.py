
class CryptoCoin:

    def __init__(self, coin, current_coin_volume, value):
        self.coin = coin  # name of the coin
        self.current_coin_volume = current_coin_volume  # = amount of units that are in circulation
        self.value = value  # = price per unit

        # Maybe will get implemented later
        # self.market_cap = market_cap  # = over all market cap of crypto currency
        # self.trading_volume = trading_volume
        # self.coin_volume = coin_volume  # = amount of units that are possible in the future
