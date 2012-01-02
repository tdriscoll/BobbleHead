from menu.base_menu import BaseMenu, BaseMenuItem

class Speed(BaseMenuItem):
    
    def __init__(self, name, milliseconds):
        """ milliseconds is time between moves. Greater is slower. """
        super(Speed, self).__init__(name)
        self.milliseconds = milliseconds
        

class Speeds(BaseMenu):
    
    _SLOW = Speed('Slow', 100)
    _MEDIUM = Speed('Medium', 20)
    _FAST = Speed('Fast', 5)
    
    ALL = [_SLOW, _MEDIUM, _FAST]
    DEFAULT = _MEDIUM
