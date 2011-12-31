from PyQt4.phonon import Phonon
from common.decorators import LazyProperty

class Song(object):
    
    def __init__(self, name, location=None):
        self.name = name
        self.location = location
        
    @LazyProperty
    def _player(self):
        return Phonon.createPlayer(Phonon.MusicCategory, Phonon.MediaSource(self.location))

    def play(self):
        if self.location:
            self._player.play()
    
    def stop(self):
        if self.location:
            self._player.stop()
    

class Songs(object):
    
    _MIDI = Song('Liberty Bell (midi sound)', r"sounds\Liberty Bell(midi sound).mp3")
    _ARMY = Song('Liberty Bell (army band)', r"sounds\Monty Python`s Flying Circus Theme 1969 - 1974.mp3")
    _MUTE = Song('Mute')
    
    ALL_SONGS = [_MIDI,_ARMY,_MUTE]
    DEFAULT_SONG = _MIDI
    
    @classmethod
    def get(cls, song_name):
        for song in cls.ALL_SONGS:
            if song.name == song_name:
                return song
