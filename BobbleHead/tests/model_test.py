from unittest.case import TestCase
from bobble.model import BobbleHeadModel, Point


class ModelTests(TestCase):
    
    def setUp(self):
        self.model = BobbleHeadModel()
    
    def increment_many(self, times):
        for x in range(times):
            self.model.increment()
    
    def test_increment_1_time(self):
        self.model.increment()
        self.assertEquals(Point(210,1),self.model.head_location)
        self.assertEquals(1,self.model.head_rotation)
    
    def test_increment_2_times_moves_twice_as_much(self):
        self.increment_many(2)
        self.assertEquals(Point(210,2),self.model.head_location)
        self.assertEquals(2,self.model.head_rotation)
    
    def test_increment_20_times_brings_me_back_to_start(self):
        self.increment_many(20)
        self.assertEquals(Point(210,0),self.model.head_location)
        self.assertEquals(0,self.model.head_rotation)

    def test_increment_25_times_rotates_backwards(self):
        self.increment_many(25)
        self.assertEquals(Point(210,5),self.model.head_location)
        self.assertEquals(-5,self.model.head_rotation)
    