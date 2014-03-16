from PyQt4.phonon import Phonon
from PyQt4.QtCore import QObject, SIGNAL
from common.lazy_property import LazyProperty

class MusicPlayer(object):
    
    def __init__(self, path):
        self.path = path

    def play(self):
        self._player.play()
        QObject.connect(self._player, SIGNAL("finished()"), self._restart);
    
    def stop(self):
        self._player.stop()
        QObject.disconnect(self._player, SIGNAL("finished()"), self._restart);
    
    @LazyProperty
    def _player(self):
        return Phonon.createPlayer(Phonon.MusicCategory, Phonon.MediaSource(self.path))
    
    def _restart(self):
        self._player.stop()
        self._player.play()
