import OpenGL as gl
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PySide2 import QtCore
from PySide2.QtWidgets import QOpenGLWidget

import math

PI = 3.14159265358979

class Render_component(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        glutInit()

        self.preDrawing()

        self.timerRender = QtCore.QTimer(self)
        self.timerRender.timeout.connect(self.paintGL)
        self.timerRender.start(34)

        self.timerUpdate = QtCore.QTimer(self)
        self.timerUpdate.timeout.connect(self.update)
        self.timerUpdate.start(12)

    def preDrawing(self):
        pass

    def paintGL(self):
        pass


    def update(self):
        pass

    def postDrawing(self):
        pass