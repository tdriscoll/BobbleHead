from PyQt4.QtGui import QGraphicsView, QPixmap, QGraphicsPixmapItem, QMainWindow, QActionGroup, QGraphicsScene, \
                        QDesktopWidget, QMatrix, QAction, QIcon, qApp
from PyQt4.QtCore import Qt
from common.decorators import LazyProperty
from bobble.songs import Songs

class BobbleHeadView(QMainWindow):
    
    BACKGROUND_IMAGE_LOCATION = r"images\background.png"
    HEAD_IMAGE_LOCATION = r"images\timhead.png"
    ICON_IMAGE_LOCATION = r'images\BobbleHead Bill_32X32.ico'
    TITLE = 'Tim Bobble Head'
    
    def render(self):
        self.create_song_menu_bar()
        
        view = QGraphicsView(self.scene)
        self.setCentralWidget(view) 
        
        #set window to size of background image, need some extra pixels to fit menu bar and crap
        self.resize(self.background_pixmap.width()+2, self.background_pixmap.height()+23) 
        self.center_window()
        self.setWindowTitle(self.TITLE)
        self.setWindowIcon(QIcon(self.ICON_IMAGE_LOCATION))    
    
    def create_song_menu_bar(self):
        """ Creates a menu.  Groups them so you can only select one at a time, """
        menuActionGroup = QActionGroup(self)
        menuActionGroup.setExclusive(True)
        menubar = self.menuBar()
        sound_menu = menubar.addMenu('Sound')
        for action in self.song_actions:
            menuActionGroup.addAction(action)
            sound_menu.addAction(action)
            
    @LazyProperty
    def song_actions(self):
        actions = []
        for song in Songs.ALL_SONGS:
            action = QAction(song.name, self)
            action.setCheckable(True)
            if song == Songs.DEFAULT_SONG:
                action.setChecked(True)
            actions.append(action)
        return actions
    
    @LazyProperty
    def background_pixmap(self):
        return QPixmap(self.BACKGROUND_IMAGE_LOCATION)
    
    @LazyProperty
    def background_pixmap_item(self):
        return QGraphicsPixmapItem(self.background_pixmap)
    
    @LazyProperty
    def head_pixmap(self):
        return QPixmap(self.HEAD_IMAGE_LOCATION)
    
    @LazyProperty   
    def head_pixmap_item(self):
        head_pixmap_item = QGraphicsPixmapItem(self.head_pixmap)
        head_pixmap_item.setZValue(1)
        return head_pixmap_item

    @LazyProperty 
    def scene(self):
        scene = QGraphicsScene()
        scene.addItem(self.background_pixmap_item)
        scene.addItem(self.head_pixmap_item)
        return scene

    def center_window(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def set_head_location(self, point, rotation):
        matrix = QMatrix()
        matrix.rotate(rotation)
        rotated_head_pixmap = self.head_pixmap.transformed(matrix)
        self.head_pixmap_item.setPixmap(rotated_head_pixmap)
        self.head_pixmap_item.setX(point.x)
        self.head_pixmap_item.setY(point.y)


    def keyPressEvent(self, ev):
        if ev.key() == Qt.Key_Escape:
            qApp.quit()