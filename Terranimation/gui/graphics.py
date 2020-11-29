#from glumpy import gloo
from PySide2 import QtCore
#from PySide2.QtOpenGLFunctions import QOpenGLFunctions_4_5_Core as gl
from PySide2.QtWidgets import QOpenGLWidget
import PySide2.Qt3DRender
#from PySide2 import Qt3DRender as gl
from PySide2.QtOpenGL import *

import ctypes
from OpenGL import GL as gl
import OpenGL.GL.shaders  as sh

import numpy as np

import glfw

import threading, time
#from glumpy import app, gloo, gl
import math


class Render_component(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        # self.timerRender = QtCore.QTimer(self)
        # self.timerRender.timeout.connect(self.paintGL)
        # self.timerRender.start(34)
        #
        # self.timerUpdate = QtCore.QTimer(self)
        # self.timerUpdate.timeout.connect(self.update)
        # self.timerUpdate.start(12)

        size = 600

        viewX = int((self.width() - size) / 2)
        viewY = int((self.height() - size) / 2)



    def initializeGL(self):

        # glfw.make_context_current(self.context().currentContext())


        self.tetra_object = [0.0, 0.5, 0.0, 1.0, 1.0, 1.0,  # red

                         0.5, -0.5, 0.0, 1.0, 1.0, 1.0,  # green
                         -0.5, -0.5, 0.0, 1.0, 1.0, 1.0]  # blue

        self.dence = 14

        #self.tetra_object = [i for i in range(0, self.dence ** 2 + 1)  ]

        self.tetra_object = np.array(self.tetra_object, dtype=np.float32)

        self.vertex_shader_source = """
            #version 330
            in vec3 position;
            in vec3 color;

            out vec3 newColor;
            void main()
            {
                gl_Position = vec4(position, 1.0f);
                newColor = color;
            }
            """
        self.fragment_shader_source = """
            #version 330
            in vec3 newColor;

            out vec4 outColor;
            void main()
            {
                outColor = vec4(newColor, 1.0f);
            }
            """

        vertex_shader = sh.compileShader(self.vertex_shader_source, gl.GL_VERTEX_SHADER)
        fragment_shader = sh.compileShader(self.fragment_shader_source, gl.GL_FRAGMENT_SHADER)
        self.shader = sh.compileProgram(vertex_shader, fragment_shader)

        self.vbo = gl.glGenBuffers(1)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.vbo)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, 72, self.tetra_object, gl.GL_STATIC_DRAW)

        self.position = gl.glGetAttribLocation(self.shader, "position")
        gl.glVertexAttribPointer(self.position, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(0))
        gl.glEnableVertexAttribArray(self.position)

        self.color = gl.glGetAttribLocation(self.shader, "color")
        gl.glVertexAttribPointer(self.color, 3, gl.GL_FLOAT, gl.GL_FALSE, 24, ctypes.c_void_p(12))

        gl.glUseProgram(self.shader)

        gl.glClearColor(0.2, 0.2, 0.2, 0.2)

    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)





        pass

    def update(self):

        pass




    def postDrawing(self):
        pass