import time; start_time = time.time()
import unittest
from bobble.presenter import BobbleHeadPresenter
from mock import Mock
print "Took", round(time.time() - start_time, 2)

class Test(unittest.TestCase):


    def setUp(self):
        self.view = Mock()
        presenter = BobbleHeadPresenter(None)


    def tearDown(self):
        pass


    def testName(self):
        #TODO: move QtCore out of BobbleHeadPresenter
        #Test bobble_the_head & initialize
        #move song stuff out http://code.activestate.com/recipes/413268/
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()