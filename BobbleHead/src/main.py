from PyQt4.QtGui import QApplication
import sys
from bobble.presenter import BobbleHeadPresenter

def main():
    app = QApplication(sys.argv)
    presenter = BobbleHeadPresenter()
    presenter.initialize()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()