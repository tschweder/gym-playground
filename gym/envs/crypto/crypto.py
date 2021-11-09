import numpy as np

from gym import Env, spaces
from gym.utils import seeding
from gym.utils.crypto_coin import CryptoCoin
import os
import os.path
import json



class CryptoEnv(Env):

    def __init__(self):
        self.action_space = spaces.Discrete(10000)  # 1 000 000.0000
        self.observation_space = spaces.Discrete(500)  # 1 000 000.0000

        self.seed()
        self.t = 0
        self.state_list = self.get_list()
        self.state = self.state_list[0]
        self.prediction = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.t = 0

    def get_list(self):
        state_list = []
        dirname = os.path.dirname(__file__)
        data_dirname = os.path.join(dirname[:-15], 'crypto\\data_collector\\crypto_crawler\\data\\')
        for name in os.listdir(data_dirname):
            with open(f'{data_dirname}{name}', 'r') as f:
                data = f.read()
            obj = json.loads(data)
            for coin in obj:
                coin_json = json.loads(coin)
                if coin_json['name'] == 'Bitcoin':
                    state_list.append(coin_json)
        return state_list

    def step(self, prediction):
        self.t += 1
        if int(prediction) != 0:
            self.prediction = prediction
        else:
            self.prediction = 1
        try:
            self.state = self.state_list[self.t]
        except Exception as exception:
            print('Out of data')
            return 0, 0, True, f'Last Prediction: {prediction}'
        pr_o = int(float(self.state_list[self.t-1]['price'][1:].replace(',', '')))
        pr_n = int(float(self.state['price'][1:].replace(',', '')))
        prediction_proportion = self.prediction / pr_o
        actual_proportion = pr_n / pr_o
        proportion = actual_proportion / prediction_proportion

        if proportion <= 1:
            reward = proportion
        else:
            reward = 1 / proportion
        # debug print(f"{self.t}: prediction " + str(prediction))
        # debug print(f"{self.t}: price old " + str(int(pr_o)))
        # debug print(f"{self.t}: price new " + str(int(pr_n)))
        # debug print(f"{self.t}: prediction pro " + str(prediction_proportion))
        # debug print(f"{self.t}: actual pro " + str(actual_proportion))
        # debug print(f"{self.t}: pro " + str(proportion))
        # debug print(f"{self.t}: " + str(self.prediction))
        return float(self.state['price'][1:].replace(',', '')), reward, False, f'Prediction: {prediction}, Actual Price:{self.state["price"]}'

    def render(self, mode="human"):

        print(self.state['name'] + " " + str(int(self.prediction)))
