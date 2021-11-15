import random

import gym
from random import randint
from gym.utils import seeding

card_colors = {
    0: 'Red',
    1: 'Green',
    2: 'Bell',
    3: 'Leaf'
}

cards = {
    0: 'Ace',
    1: '10',
    2: 'King',
    3: 'Queen',
    4: 'Jack'
}

class SchnapsenEnv(gym.Env):

    def __init__(self):
        self.deck = []
        self.players_hand_cards = []
        self.trump = []
        self.forehand = None
        self.player = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        # TODO
        pass

    def reset(self, winner=None):
        if winner is None:
            self.forehand = random.choice([True, False])
        else:
            if winner:
                self.forehand = True
            else:
                self.forehand = False
        if self.forehand:
            self.player = 0
        else:
            self.player = 1
        self.game_start()

    def game_start(self):
        self.shuffle_deck()
        self.players_hand_cards = self.draw_from_deck(3)
        self.players_hand_cards.append(self.draw_from_deck(3))
        self.trump = self.draw_from_deck(1)[0]
        for x in range(2):
            self.players_hand_cards[0].append(self.draw_from_deck(1)[0])
        for y in range(2):
            self.players_hand_cards[1].append(self.draw_from_deck(1)[0])

    def draw_from_deck(self, num_of_cards):
        if num_of_cards > len(self.deck) + len(self.trump):
            print("Error, could not draw that many cards!")
        card_list = []
        for x in range(num_of_cards):
            card_list[x] = self.deck[x]
        for i in range(len(card_list)):
            self.deck.pop(i)
        return card_list


    def shuffle_deck(self):
        self.deck = []
        x = 0
        while len(self.deck) < 20:
            c = randint(0, 4)
            cc = randint(0, 3)
            card = [cards[c], card_colors[cc]]
            if card not in self.deck:
                self.deck[x] = card
                x += 1

