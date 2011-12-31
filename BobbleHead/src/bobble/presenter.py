from bobble.model import BobbleHeadModel
from bobble.view import BobbleHeadView
from PyQt4 import QtCore
from functools import partial

class BobbleHeadPresenter(object):
    
    MILISECONDS_BETWEEN_HEAD_MOVES = 10
    
    def __init__(self):
        self.model = BobbleHeadModel()
        self.view = BobbleHeadView()
    
    def initialize(self):
        #Start up screen
        self.view.render()
        self.synch_head_location()
        
        self.start_head_mover()
        self.model.play_current_song()

        self.register_callbacks()
        
        self.view.show()
        
    def start_head_mover(self):
        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.bobble_the_head)
        self.timer.start(self.MILISECONDS_BETWEEN_HEAD_MOVES)
        
    def register_callbacks(self):
        for menu_action in self.view.song_actions:
            menu_action.triggered.connect(partial(self.model.change_song, str(menu_action.text())))
    
    def bobble_the_head(self):
        self.model.increment()
        self.synch_head_location()
        
    def synch_head_location(self):
        self.view.set_head_location(self.model.head_location, self.model.head_rotation)
        