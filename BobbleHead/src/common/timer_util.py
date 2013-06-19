from PyQt4.QtCore import QTimer, QObject, SIGNAL

class TimerUtil(object):

    @classmethod
    def create_timer(cls, call_me):
        timer = QTimer()
        QObject.connect(timer, SIGNAL("timeout()"), call_me)
        return timer
