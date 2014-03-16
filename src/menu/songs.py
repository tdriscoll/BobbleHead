from menu.base_menu import BaseMenu, BaseMenuItem
from common.file_location import FileLocation
from common.lazy_property import LazyProperty

class Song(BaseMenuItem):
    
    music_player = None
    
    def __init__(self, name, location=None):
        super(Song, self).__init__(name)
        self.location = location
        
    @LazyProperty
    def _player(self):
        return self.music_player(self.location)

    def play(self):
        if self.location:
            self._player.play()
    
    def stop(self):
        if self.location:
            self._player.stop()
    

class Songs(BaseMenu):
    
    _MIDI = Song('Liberty Bell (midi sound)', FileLocation.MIDI)
    _ARMY = Song('Liberty Bell (army band)', FileLocation.ARMY)
    _VOCAB = Song('Abeyance', FileLocation.VOCAB)
    _MUTE = Song('Mute')
    
    ALL     = [_MIDI,_ARMY, _VOCAB, _MUTE]
    DEFAULT = _MIDI
    
