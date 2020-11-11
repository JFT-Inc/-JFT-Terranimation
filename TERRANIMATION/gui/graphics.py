from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLUT.freeglut import *

import OpenGL.GL.shaders as shaders
from PySide2 import QtCore
from PySide2.QtOpenGLFunctions import QOpenGLFunctions_4_5_Core as gl
from PySide2.QtWidgets import QOpenGLWidget

from PySide2.QtOpenGL import *

import threading, time

import math

#Git test

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

        self.triger = 0

    def preDrawing(self):
        pass

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.2, 0.2, 0.2)

        glBegin(GL_POLYGON)
        glColor3d(0, 1, 1)
        glVertex2d(-0.5, -0.5)
        glVertex2d(-0.5, 0.5)
        glColor3d(1, 0, 1)
        glVertex2d(0.5, 0.5)
        glVertex2d(1, -0.5)
        glEnd()



    def update(self):
        pass

    def postDrawing(self):
        pass