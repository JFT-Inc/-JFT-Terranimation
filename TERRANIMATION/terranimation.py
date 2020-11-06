# Copyright ⓒ Nefty 2020 WTFPL
#
# Main application file for starting app!
#
# The app runs like this...
#
#   File system           data to application
#            QT                          Start GL -> Just Go --------------------------------------->
#        Render                          Rendering -> render data updates as event happens --------->
# Terranimation  Start -> Get momentum,  Start Qt, create objects -> updating objects -------------->
#   Object data           Objects created. holding momentum data --> updated ----------------------->
# 
# Application owns every thing. but it is your duty to start and keep the application.

from PySide2.QtWidgets import *
from PySide2.QtGui import *

import sys
import threading as thrd

from TERRANIMATION import event
from TERRANIMATION.gui import *


# Application it self
class Terranimation:
    event_engine = None

    def closeProgram(self):
        self.run = False

    def __init__(self, x=None, y=None, w=None, h=None):
        print("Wellcome to Terranimation!")

        #Start QtApplication
        self.application = QApplication()

        print("Prepare to go")

        # Application data
        self.dimension: list[int] = [x, y, w, h]
        self.title = "Terranimation"
        self.framerate = 30
        self.filedata = None
        self.run = True
        self.registry = {}
        self.loop = thrd.Thread(target=self.update, args=())

        # Graphical object data
        self.vertexs = []
        self.vectors = []
        self.images = None

        # Gui Ready!
        self.app_window = NewQWidget(self.application)
        self.app_window.setWindowTitle(self.title)
        self.app_window.show()


        # Event setup
        self.event_engine = event.EventSquenceHandler()
        self.event_engine.registerEvent(lambda param: param.close, event.ButtonPressedEvent)

        # add event to system
        self.app_window.addCloseEvent(self.exit)

        self.application.exec_()

    def update(self):
        while self.run:
            pass

        return self

    def show(self):
        self.app_window.show()

    def isRunning(self):
        return self.run

    def register(self, param_registry):
        pass

    def boot(self):
        self.loop.start()
        self.loop.join()
        pass

    def exit(self):
        print("!!!!!!!!!!!!!")

        self.application.exit()
        self.run = False

if __name__ == "__main__":
    t = Terranimation(w=100)
    t.show()
    t.boot()

    print("My work is done!")
