import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(".."))
import player

class TestPlayerAvalableLocation(unittest.TestCase):
    def setUp(self):
        self.player = player.Player()
        self.board_block_location = [
        (0,0), (0,1), (0,5),
        (1,0), (1,6), (1,11),
        (2,4), (2,10), (2,11)]

    def test_init(self):
        for y in range(3):
            for x in range(12):
                if((y,x)  not in self.board_block_location):
                    self.assertTrue(self.player.is_location_ok(2,x,y), "param: %d %d" % (x, y))
                else:
                    self.assertFalse(self.player.is_location_ok(2,x,y), "param: %d %d" % (x, y))

    def test_fill_2_3_0(self):
        self.player.accept_roll(2, 3, 0)
        self.assertEqual(self.player.check_location_conflict(2, 3, 0), 1, "occupied conflict test")
        self.assertEqual(self.player.check_location_conflict(2, 3, 1), 4, "column conflict test")
        self.assertEqual(self.player.check_location_conflict(2, 2, 0), 2, "row conflict test")
        self.assertEqual(self.player.check_location_conflict(3, 2, 0), 3, "order conflict test")
        self.assertEqual(self.player.check_location_conflict(1, 4, 0), 3, "order conflict test")

    def test_score_43(self):
        self.player.accept_roll(7,2,0)
        self.player.accept_roll(8,3,0)
        self.player.accept_roll(9,4,0)
        self.player.accept_roll(10,6,0)
        self.player.accept_roll(11,7,0)
        self.player.accept_roll(12,8,0)
        self.player.accept_roll(13,9,0)
        self.player.accept_roll(14,10,0)
        self.player.accept_roll(15,11,0)

        self.player.accept_roll(2,1,1)
        self.player.accept_roll(4,2,1)
        self.player.accept_roll(11,5,1)
        self.player.accept_roll(12,7,1)
        self.player.accept_roll(13,8,1)

        self.player.accept_roll(2,0,2)
        self.player.accept_roll(5,1,2)
        self.player.accept_roll(8,2,2)
        self.player.accept_roll(10,5,2)
        self.player.accept_roll(11,6,2)
        self.player.accept_roll(14,8,2)
        self.player.accept_roll(15,9,2)

        self.player.fail()

        self.assertEqual(self.player.calculate_score(), 43, "score not right")
