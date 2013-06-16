from PyQt4.phonon import Phonon
from common.decorators import LazyProperty
from PyQt4.QtCore import QObject, SIGNAL
from menu.base_menu import BaseMenu, BaseMenuItem
from common.file_location import FileLocation

class Song(BaseMenuItem):
    
    def __init__(self, name, location=None):
        super(Song, self).__init__(name)
        self.location = location
        
    @LazyProperty
    def _player(self):
        return Phonon.createPlayer(Phonon.MusicCategory, Phonon.MediaSource(self.location))

    def play(self):
        if self.location:
            self._player.play()
            QObject.connect(self._player, SIGNAL("finished()"), self.restart);
    
    def stop(self):
        if self.location:
            self._player.stop()
            QObject.disconnect(self._player, SIGNAL("finished()"), self.restart);
    
    def restart(self):
        self._player.stop()
        self._player.play()

class Songs(BaseMenu):
    
    _MIDI = Song('Liberty Bell (midi sound)', FileLocation.MIDI)
    _ARMY = Song('Liberty Bell (army band)', FileLocation.ARMY)
    _VOCAB = Song('Abeyance', FileLocation.VOCAB)
    _MUTE = Song('Mute')
    
    ALL     = [_MIDI,_ARMY, _VOCAB, _MUTE]
    DEFAULT = _MIDI
    
