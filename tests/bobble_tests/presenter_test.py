import time; start_time = time.time()
import unittest
from bobble.presenter import BobbleHeadPresenter
from mock import Mock
from menu.songs import Song
from quiet_music_player import QuietMusicPlayer
from testy_timer_util import TestyTimerUtil
from bobble.model import Point
from common.file_location import FileLocation
print "Took", round(time.time() - start_time, 2)

class BobbleHeadPresenterTest(unittest.TestCase):


    def setUp(self):
        BobbleHeadPresenter.timer_util = TestyTimerUtil
        Song.music_player = QuietMusicPlayer
        self.view = Mock()
        self.view.song_actions = []
        self.view.speed_actions = []
        self.presenter = BobbleHeadPresenter(self.view)

    def tearDown(self):
        QuietMusicPlayer.CURRENTLY_PLAYING = None

    def test_initialize_everything(self):
        self.presenter.initialize()
        self.assertEquals(3, len(self.view.method_calls))
        self.view.render.assert_called_once_with()
        self.view.set_head_location.assert_called_once_with(Point(210, 0), 0)
        self.view.show.assert_called_once_with()
        self.assertEquals(20, self.presenter.timer.speed)
        self.assertEquals(FileLocation.MIDI, QuietMusicPlayer.CURRENTLY_PLAYING)

    def test_bobbling_a_few_times(self):
        self.presenter.initialize()
        self.view.reset_mock()
        self.presenter.bobble_the_head()
        self.view.set_head_location.assert_called_with(Point(210, 1), 1)
        self.presenter.bobble_the_head()
        self.view.set_head_location.assert_called_with(Point(210, 2), 2)
        
