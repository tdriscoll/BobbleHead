from bobble.songs import Songs


class BobbleHeadModel(object):
    
    def __init__(self):
        self.head_location = Point(210, 0) #starting point of head (middle of body near neck)
        self.head_rotation= 0
        self.moving_down = True
        self.spinning_right = True
        self.current_song = Songs.DEFAULT_SONG
        
    def increment(self):
        if self.head_location.y == 10:
            self.moving_down = False
        elif self.head_location.y == 0:
            self.moving_down = True
        
        if self.head_rotation == 10:
            self.spinning_right = False
        elif self.head_rotation == -10:
            self.spinning_right = True
        
        y_delta = 1 if self.moving_down else -1
        rotation_delta =  1 if self.spinning_right else -1
        
        self.head_location = Point(self.head_location.x,self.head_location.y+y_delta)
        self.head_rotation += rotation_delta
        
    def change_song(self, song_name):
        self.current_song.stop()
        self.current_song = Songs.get(song_name)
        self.current_song.play()
    
    def play_current_song(self):
        self.current_song.play()
        


class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return "<Point %s, %s>" % (self.x, self.y)
    
    __repr__ = __str__
        