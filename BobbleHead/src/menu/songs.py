from PyQt4.phonon import Phonon
from common.decorators import LazyProperty
from PyQt4.QtCore import QObject, SIGNAL
from menu.base_menu import BaseMenu, BaseMenuItem

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
    
    _MIDI = Song('Liberty Bell (midi sound)', r"sounds\Liberty Bell(midi sound).mp3")
    _ARMY = Song('Liberty Bell (army band)', r"sounds\Monty Python`s Flying Circus Theme 1969 - 1974.mp3")
    _VOCAB = Song('Abeyance', r"sounds\05 abeyance _ temporary inactivity or suspension.mp3")
    _MUTE = Song('Mute')
    
    ALL     = [_MIDI,_ARMY, _VOCAB, _MUTE]
    DEFAULT = _MIDI
    
