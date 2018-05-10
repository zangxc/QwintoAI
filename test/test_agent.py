import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(".."))
import agent

class TestAgentAvalableLocation(unittest.TestCase):
    def setUp(self):
        self.agent = agent.Agent()
        self.board_block_location = [
        (0,0), (0,1), (0,5),
        (1,0), (1,6), (1,11),
        (2,4), (2,10), (2,11)]

    def test_init(self):

        for y in range(3):
            for x in range(12):
                if((y,x)  not in self.board_block_location):
                    self.assertTrue(self.agent.is_location_ok(2,x,y), "param: %d %d" % (x, y))
                else:
                    self.assertFalse(self.agent.is_location_ok(2,x,y), "param: %d %d" % (x, y))
