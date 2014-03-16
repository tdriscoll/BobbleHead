from bobble.model import BobbleHeadModel
from functools import partial
from menu.speeds import Speeds

class BobbleHeadPresenter(object):
    
    MILISECONDS_BETWEEN_HEAD_MOVES = 10
    timer_util = None
    
    def __init__(self, view):
        self.view = view
        self.model = BobbleHeadModel()
        self.timer = None
    
    def initialize(self):
        #Start up screen
        self.view.render()
        self.synch_head_location()
        
        self.start_head_mover()
        self.model.play_current_song()

        self.register_callbacks()
        
        self.view.show()
        
    def start_head_mover(self):
        self.timer = self.timer_util.create_timer(self.bobble_the_head)
        self.timer.start(Speeds.DEFAULT.milliseconds)  # @UndefinedVariable
    
    def register_callbacks(self):
        for menu_action in self.view.song_actions:
            menu_action.triggered.connect(partial(self.model.change_song, str(menu_action.text())))
            
        for menu_action in self.view.speed_actions:
            menu_action.triggered.connect(partial(self.change_speed, str(menu_action.text())))
    
    
    def bobble_the_head(self):
        self.model.increment()
        self.synch_head_location()
        
    def synch_head_location(self):
        self.view.set_head_location(self.model.head_location, self.model.head_rotation)
        
    def change_speed(self, speed_name):
        self.timer.stop()
        self.timer.start(Speeds.get(speed_name).milliseconds) 
        