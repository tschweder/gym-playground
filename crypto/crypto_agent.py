import numpy as np
import gym
from gym.wrappers import record_episode_statistics
from gym.utils.crypto_coin import CryptoCoin
import random


def main():

    coin = CryptoCoin(
            coin="BTC",
            market_cap=300,
            trading_volume=10,
            current_coin_volume=500,
            coin_volume=1000,
            value=0.2
    )
    env = gym.make(id="Crypto-v1", coin=coin, )
    env = record_episode_statistics(env)

    # initialize q-table
    state_size = env.observation_space.n
    action_size = env.action_space.n
    qtable = np.zeros((state_size, action_size))

    # hyperparameters
    learning_rate = 0.9
    discount_rate = 0.8
    epsilon = 1.0
    decay_rate = 0.01
    state_list = env.reset()

    for e in 101:
        if random.uniform(0, 1) < epsilon:
            # explore
            action = env.action_space.sample()
        else:
            action = np.argmax(qtable[state, :])
        prediction, reward, done, info = env.step(action)
        qtable[state, action] = qtable[state, action] + learning_rate * (
                    reward + discount_rate * np.max(qtable[prediction, :]) - qtable[state, action])
        state = state_list[e]
        epsilon -= decay_rate
    env.render()


if __name__ == "__main__":
    main()
