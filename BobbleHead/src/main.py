from PyQt4 import QtGui
import sys
from bobble.presenter import BobbleHeadPresenter

def main():
    app = QtGui.QApplication(sys.argv)
    presenter = BobbleHeadPresenter()
    presenter.initialize()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()