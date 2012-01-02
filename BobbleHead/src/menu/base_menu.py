
class BaseMenuItem(object):
    
    def __init__(self, name):
        self.name = name

class BaseMenu(object):
    """ Base class for a group of menu items """
    
    ALL = []
    DEFAULT = None
    
    @classmethod
    def get(cls, menu_item_name):
        for menu_item in cls.ALL:
            if menu_item.name == menu_item_name:
                return menu_item
