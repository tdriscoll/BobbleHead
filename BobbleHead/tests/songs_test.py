from unittest.case import TestCase
from bobble.songs import Songs


class SongsTests(TestCase):
    
    def test_get_song_by_name(self):
        expected = Songs._ARMY
        actual = Songs.get('Liberty Bell (army band)')
        self.assertEquals(expected, actual)