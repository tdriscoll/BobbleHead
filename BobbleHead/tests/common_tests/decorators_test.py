from unittest.case import TestCase
from common.decorators import LazyProperty


class TestMe(object):
    
    def __init__(self):
        self.number_calls = 0
        
    @LazyProperty
    def lazy(self):
        self.number_calls += 1
        return self.number_calls

class DecoratorTests(TestCase):
    
    def test_lazy_property_only_called_once(self):
        t = TestMe()
        self.assertEquals(0,t.number_calls)
        self.assertEquals(1,t.lazy)
        self.assertEquals(1,t.lazy)
        del t.lazy
        self.assertEquals(2,t.lazy)
        
        t2 = TestMe()
        self.assertEquals(0,t2.number_calls)
        self.assertEquals(1,t2.lazy)
        self.assertEquals(1,t2.lazy)
        
        