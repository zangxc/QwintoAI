import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(".."))
import game


class TestGameRoll(unittest.TestCase):
    def test_roll_all(self):
        g = game.Game(4)
        for _ in range(0,100):
            number, red, yellow, blue = g.roll(True,True,True)
            # print(number, red, yellow, blue)
            self.assertIn(number, range(3,19))
            self.assertTrue(red)
            self.assertTrue(yellow)
            self.assertTrue(blue)
    def test_roll_red_yellow(self):
        g = game.Game(4)
        for _ in range(0,100):
            number, red, yellow, blue = g.roll(True,True,False)
            # print(number, red, yellow, blue)
            self.assertIn(number, range(2,13))
            self.assertTrue(red)
            self.assertTrue(yellow)
            self.assertFalse(blue)
    def test_roll_blue(self):
        g = game.Game(4)
        for _ in range(0,100):
            number, red, yellow, blue = g.roll(False,False,True)
            # print(number, red, yellow, blue)
            self.assertIn(number, range(1,7))
            self.assertFalse(red)
            self.assertFalse(yellow)
            self.assertTrue(blue)

class TestGameTurn(unittest.TestCase):
    def test_init(self):
        g = game.Game(4)
        self.assertTrue(g.is_my_turn())
    def test_60_step(self):
        g = game.Game(4)
        for _ in range(60):
            g.finish_turn()
        self.assertTrue(g.is_my_turn())
    def test_6_step(self):
        g = game.Game(4)
        for _ in range(6):
            g.finish_turn()
        self.assertFalse(g.is_my_turn())
