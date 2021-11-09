import numpy as np
import gym
import random
import os
import os.path

def main():

    env = gym.make(id="Crypto-v1")

    # initialize q-table
    state_size = env.observation_space.n
    action_size = env.action_space.n
    qtable = np.zeros((state_size, action_size))

    # hyperparameters
    learning_rate = 0.9
    discount_rate = 0.8
    epsilon = 1.0
    decay_rate = 0.00225
    state_list = env.get_list()
    env.reset()
    for e in range(len([name for name in os.listdir('./data_collector/crypto_crawler/data/')]) - 1):
        if random.uniform(0, 1) < epsilon:
            # explore
            action = env.action_space.sample()
        else:
            # exploit
            action = np.argmax(qtable[e, :])

        obs, reward, done, info = env.step(action)
        qtable[e, action] = qtable[e, action] + learning_rate * (
                    reward + discount_rate * np.max(qtable[e+1, :]) - qtable[e, action])

        epsilon -= decay_rate
    env.render()


if __name__ == "__main__":
    main()
