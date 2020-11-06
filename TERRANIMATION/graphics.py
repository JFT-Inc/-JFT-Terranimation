import OpenGL as gl
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PySide2 import QtCore
from PySide2.QtWidgets import QOpenGLWidget

import numpy
import threading, time

import math

PI = 3.14159265358979

triangle = numpy.array([0.0,  0.5, 0.0, 1.0, 0.0, 0.0, # red
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0, # green
            0.5, -0.5, 0.0, 0.0, 0.0, 1.0]) # blue

VBO = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)



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

        #glDrawArrays(GL_TRIANGLES, 0, 3)

        # print("jhkl" + str(self.a))

        time.sleep(0.5)

        glBegin(GL_POLYGON)
        glColor3d(0, 1, 1)
        glVertex2d( -0.5,-0.5  )
        glVertex2d( -0.5, 0.5  )
        glColor3d(1, 0, 1)
        glVertex2d(  0.5, 0.5  )
        glVertex2d(  self.triger, -0.5  )
        glEnd()

        print(self.triger)

        if self.triger == 0:
            self.triger = 1
        else:
            self.triger = 0



    def update(self):
        pass

    def postDrawing(self):
        pass