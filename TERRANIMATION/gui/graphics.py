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
        self.timerRender = QtCore.QTimer(self)
        self.timerRender.timeout.connect(self.paintGL)
        self.timerRender.start(34)

        self.timerUpdate = QtCore.QTimer(self)
        self.timerUpdate.timeout.connect(self.update)
        self.timerUpdate.start(12)

        self.triger = 0
        size = 600

        viewX = int((self.width() - size) / 2)
        viewY = int((self.height() - size) / 2)

        glViewport(viewX, viewY, size, size)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0.2, 0.2, 0.2, 0.2)

        # glBegin(GL_POLYGON)
        # glColor3d(0, 1, 1)
        # glVertex2d(-0.5, -0.5)
        # glVertex2d(-0.5, 0.5)
        # glColor3d(1, 0, 1)
        # glVertex2d(0.5, 0.5)
        # glVertex2d(1, -0.5)
        
        PI = 3.14159265358979

        dens = 14

        glLineWidth(6)

        glColor3d(0.0, 0.8, 0.8)
        glBegin(GL_LINE_STRIP)

        size /= 2

        point = int(dens / 2)

        a = 0
        b = 0
        c = 0

        for quarry in range(0, int(dens / 2 + 1)) :
            glVertex3d(math.cos((PI / dens) * point), math.sin((PI / dens) * point), math.cos((PI / dens) * point))

            point += 1

            # if quarry % 3 == 0:
            #     pass
            # elif quarry % 2 == 0:
            #     pass
            # else:
            #
            
        glEnd()



    def update(self):
        pass

    def postDrawing(self):
        pass