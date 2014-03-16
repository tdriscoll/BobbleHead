

class TestyTimerUtil(object):
    
    @classmethod
    def create_timer(cls, call_me):
        return TestyTimer(call_me)
    
class TestyTimer(object):
    
    STOPPED = -1
    
    def __init__(self, call_me):
        self.call_me = call_me
        self.speed = self.STOPPED
        
    def start(self, speed):
        self.speed = speed
        
    def stop(self):
        self.speed = self.STOPPED