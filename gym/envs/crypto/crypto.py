import numpy as np

from gym import Env, spaces
from gym.utils import seeding
# from gym.utils.crypto_coin import CryptoCoin


class CryptoEnv(Env):

    def __init__(self, coin):
        self.action_space = spaces.Discrete(1000000.0000)  # 1 000 000.0000
        self.observation_space = spaces.Discrete(1000000.0000)  # 1 000 000.0000

        self.seed()

        self.coin = coin
        self.prediction = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        pass

    def step(self, action):
        pass

    def render(self, mode="human"):
        print(self.coin.coin + " " + self.prediction)
