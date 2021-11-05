
class CryptoCoin:

    def __init__(self, coin, market_cap, trading_volume, current_coin_volume, coin_volume, value):
        self.coin = coin
        self.market_cap = market_cap  # = over all market cap of crypto currency
        self.trading_volume = trading_volume
        self.current_coin_volume = current_coin_volume  # = amount of units that are in circulation
        self.current_coin_volume = coin_volume  # = amount of units that are possible in the future
        self.value = value  # = price per unit
