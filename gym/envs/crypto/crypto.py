import numpy as np

from gym import Env, spaces
from gym.utils import seeding


class CryptoEnv(Env):

    def __init__(self):
        pass

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        pass

    def step(self, a):
        pass