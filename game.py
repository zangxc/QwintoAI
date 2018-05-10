import random

class Game(object):

    def __init__(self, player_number):
        self.player_index = 0
        self.player_number = player_number;

    def roll(self,red,yellow,blue):
        sum = 0
        if red:
            sum = sum + random.randint(1,6)
        if yellow:
            sum = sum + random.randint(1,6)
        if blue:
            sum = sum + random.randint(1,6)
        return (sum,red,yellow,blue)

    def is_my_turn(self):
        return self.player_index == 0;

    def finish_turn(self):
        self.player_index = (self.player_index + 1) % self.player_number
