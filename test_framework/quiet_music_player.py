class QuietMusicPlayer(object):
    
    CURRENTLY_PLAYING = None
    
    def __init__(self, path):
        self.path = path
    
    def play(self): 
        QuietMusicPlayer.CURRENTLY_PLAYING = self.path
        
