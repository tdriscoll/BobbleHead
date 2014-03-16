from PyQt4.QtGui import QApplication
import sys
from bobble.presenter import BobbleHeadPresenter
from common.constants import Application
from bobble.view import BobbleHeadView
from common.timer_util import TimerUtil
from common.music_player import MusicPlayer
from menu.songs import Song

def inject_dependencies():
    BobbleHeadPresenter.timer_util = TimerUtil
    Song.music_player = MusicPlayer

def main():
    inject_dependencies()
    app = QApplication(sys.argv)
    app.setApplicationName(Application.NAME)
    view = BobbleHeadView()
    presenter = BobbleHeadPresenter(view)
    presenter.initialize()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()