from PySide2 import QtWidgets
from PySide2.QtCore import QObject
from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QCloseEvent

from TERRANIMATION.graphics import Render_component
from TERRANIMATION import event as _event
from TERRANIMATION import terranimation as app

class NewQWidget(QWidget):
    screen_geometry = None
    screen_partial = None
    callback_dict = {}

    def __init__(self, qtapp, x=None, y=None, w=None, h=None):
        super(NewQWidget, self).__init__()
        print("QT5!")
        # Qt5 setup
        self.screen_geometry = qtapp.primaryScreen().geometry()
        self.screen_partial = (self.screen_geometry.width() / 100, self.screen_geometry.height() / 100)

        # initial windows setting!
        afunc = lambda a, b: int(b if a == None else a)
        w = afunc(w, self.screen_partial[0] * 80); #self.geometry().setWidth(w)
        h = afunc(h, self.screen_partial[1] * 80); #self.geometry().setHeight(h)
        x = afunc(x, self.screen_geometry.width() / 2 - w / 2); self.geometry().setX(x)
        y = afunc(y, self.screen_geometry.height() / 2 - h / 2); self.geometry().setY(y)

        # Layout and components
        self.component:list(QObject) = []

        self.widget_area = QtWidgets.QScrollArea()
        self.widget_area.setGeometry(x, y, w, h)
        self.component.append(Render_component())

        self.layoutManager = QtWidgets.QGridLayout()
        for item in self.component:
            self.layoutManager.addWidget(item)
        self.setLayout(self.layoutManager)

        self.resize(w, h)

    def addCloseEvent(self, callback, *args):
        self.callback_dict[callback] = args

        #print("!!!: " + str(callback) + " : "+ str(args))

    def closeEvent(self, event:QCloseEvent):
        for key in list(self.callback_dict.keys()):
            key(*self.callback_dict[key])
        #app.t.event_engine.happen(_event.UiEvent(_event.EVENT_UI_CLOSING))

