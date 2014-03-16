from PyQt4.QtGui import QGraphicsView, QPixmap, QGraphicsPixmapItem, QMainWindow, QActionGroup, QGraphicsScene, \
                        QDesktopWidget, QMatrix, QAction, QIcon, qApp
from PyQt4.QtCore import Qt
from menu.songs import Songs
from menu.speeds import Speeds
from common.constants import Application
from common.file_location import FileLocation
from common.lazy_property import LazyProperty

class BobbleHeadView(QMainWindow):
#     
    def render(self):
        self.create_menu('Sound', self.song_actions)
        self.create_menu('Speed', self.speed_actions)
        
        view = QGraphicsView(self.scene)
        self.setCentralWidget(view) 
        
        #set window to size of background image, need some extra pixels to fit menu bar and crap
        #TODO: Do not need this on Ubuntu
        self.resize(self.background_pixmap.width()+2, self.background_pixmap.height()+23) 
        
        self.center_window()
        self.setWindowTitle(Application.NAME)
        self.setWindowIcon(QIcon(FileLocation.ICON_IMAGE_LOCATION))    
    
    def create_menu(self, menu_name, menu_actions):
        """ Creates a menu.  Groups them so you can only select one at a time. """
        menu_action_group = QActionGroup(self)
        menu_action_group.setExclusive(True)
        menubar = self.menuBar()
        menu = menubar.addMenu(menu_name)
        for action in menu_actions:
            menu_action_group.addAction(action)
            menu.addAction(action)
    
    @LazyProperty
    def song_actions(self):
        return self.get_actions(Songs)
    
    @LazyProperty
    def speed_actions(self):
        return self.get_actions(Speeds)
        
    def get_actions(self, menu_class):
        actions = []
        for menu_item in menu_class.ALL:
            action = QAction(menu_item.name, self)
            action.setCheckable(True)
            if menu_item == menu_class.DEFAULT:
                action.setChecked(True)
            actions.append(action)
        return actions
    
    
    @LazyProperty
    def background_pixmap(self):
        return QPixmap(FileLocation.BACKGROUND_IMAGE_LOCATION)
    
    @LazyProperty
    def background_pixmap_item(self):
        return QGraphicsPixmapItem(self.background_pixmap)
    
    @LazyProperty
    def head_pixmap(self):
        return QPixmap(FileLocation.HEAD_IMAGE_LOCATION)
    
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