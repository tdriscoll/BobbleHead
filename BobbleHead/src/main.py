from PyQt4.QtGui import QApplication
import sys
from bobble.presenter import BobbleHeadPresenter
from common.constants import Application
from bobble.view import BobbleHeadView

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(Application.NAME)
    view = BobbleHeadView()
    presenter = BobbleHeadPresenter(view)
    presenter.initialize()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()