from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def curve(p0=(0,0),p1=(1,1),p2=(1,0),p3=(0,1)):
    for t in np.arange(0, 1, 0.001):
        x=((1-t)**3)*p0[0]+((1-t)**2)*3*t*p1[0]+(1-t)*3*t*t*p2[0]+t*t*t*p3[0]
        y=((1-t)**3)*p0[1]+((1-t)**2)*3*t*p1[1]+(1-t)*3*t*t*p2[1]+t*t*t*p3[1]
        glVertex(x, y)

def draw():
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

# ears
    glLineWidth(2.0)
    glBegin(GL_POLYGON)
    glColor3f(.545, .784, .933)
    curve((0.2836, 0.276), (0.38, 0.312), (0.506, 0.256), (0.3376, 0.083))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.545, .784, .933)
    curve((0.024,0.392),(0.094,0.4695),(0.171,0.423),(0.1594,0.352))
    glEnd()

    #border
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    curve((0.2836, 0.276), (0.38, 0.312), (0.506, 0.256), (0.3376, 0.083))
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    curve((0.024, 0.392), (0.094, 0.4695), (0.171, 0.423), (0.1594, 0.352))
    glEnd()

#head
    #filling
    glBegin(GL_POLYGON)
    glColor3f(.545, .784, .933)
    curve((0.31, 0), (0.291, -0.08), (0.17, -0.171), (0, -0.12))
    curve((0.31, 0), (0.382, 0.139), (0.358, 0.354), (0, 0.39))
    curve((-0.198, 0.207), (-0.193, 0.268), (-0.104, 0.393), (0, 0.39))
    curve((-0.198, 0.207), (-0.378, 0.182), (-0.362, -0.073), (-0.0977, -0.098))
    glVertex(-0.1, -0.126)
    glVertex(-0.004, - 0.124)
    glEnd()

    #border
    glBegin(GL_LINE_LOOP)
    glColor3f( 0,0 , 0)
    curve((0, -0.12), (0.17, -0.171),(0.291, -0.08),(0.31, 0) )
    curve((0.31, 0), (0.382, 0.139), (0.358, 0.354), (0, 0.39))
    curve((0, 0.39), (-0.104, 0.393),(-0.193, 0.268) ,(-0.198, 0.207) )
    curve((-0.198, 0.207), (-0.378, 0.182), (-0.362, -0.073), (-0.0977, -0.098))
    glVertex(-0.1, -0.126)
    glVertex(-0.004, - 0.124)
    glEnd()

#eyes
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    curve((0.227,0.102),(0.318,0.246),(0.154,0.328),(0.085,0.195))
    curve((0.085,0.195),(-0.026,0.049),(0.147,-0.064),(0.227,0.102))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    curve((0.1166,0.1756),(0.034,0.049),(0.156,0.0036),(0.2,0.125))
    curve((0.2,0.125),(0.2425,0.188),(0.181,0.2754),(0.1166,0.1756))
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    curve((0.227, 0.102), (0.318, 0.246), (0.154, 0.328), (0.085, 0.195))
    curve((0.085, 0.195), (-0.026, 0.049), (0.147, -0.064), (0.227, 0.102))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    curve((-0.103, 0.26), (-0.205, 0.122), (-0.039, 0.034), (0.039, 0.19))
    curve((0.039, 0.19), (0.12, 0.331), (-0.06, 0.387), (-0.103, 0.26))
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    curve((-0.103, 0.26), (-0.205, 0.122), (-0.039, 0.034), (0.039, 0.19))
    curve((0.039, 0.19), (0.12, 0.331), (-0.06, 0.387), (-0.103, 0.26))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    curve((-0.068,0.246),(-0.033,0.326),(0.062,0.2795),(0.009,0.202))
    curve((0.009,0.202),(-0.018,0.093),(-0.148,0.1125),(-0.068,0.246))
    glEnd()

#mouth
    glBegin(GL_POLYGON)
    glColor3f(.9, .46, .45)
    curve((-0.081, 0.067), (-0.141, -0.121), (0.003, -0.112), (0.033, 0.016))
    curve((0.0155, 0.058), (0.003, 0.046), (-0.061, 0.05), (-0.081, 0.067))
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    curve((-0.081, 0.067), (-0.141, -0.121), (0.003, -0.112), (0.033, 0.016))
    curve((0.0155, 0.058), (0.003, 0.046), (-0.061, 0.05), (-0.081, 0.067))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    glVertex(0.033, 0.016)
    glVertex(0.0155, 0.058)
    glVertex(0.049, 0.064)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    glVertex(0.033, 0.016)
    glVertex(0.0155, 0.058)
    glVertex(0.049, 0.064)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)
    curve((-0.093, 0.089), (-0.08, 0.042), (0.003, 0.046), (0.049, 0.064))
    curve((-0.093, 0.089), (-0.062, 0.115), (0.035, 0.078), (0.049, 0.064))
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    curve((-0.093, 0.089), (-0.08, 0.042), (0.003, 0.046), (0.049, 0.064))
    curve((0.049, 0.064), (0.035, 0.078), (-0.062, 0.115), (-0.093, 0.089))
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.86,0.27,0.06)
    curve((-0.047, 0.093), (-0.027, 0.1), (0.001, 0.0863), (0.0133, 0.082))
    curve((0.0133, 0.082), (-0.014, 0.0666), (-0.046, 0.077), (-0.047, 0.093))
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    curve((-0.047, 0.093), (-0.027, 0.1), (0.001, 0.0863), (0.0133, 0.082))
    curve((0.0133, 0.082), (-0.014, 0.0666), (-0.046, 0.077), (-0.047, 0.093))
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.95,0.72,0.68)
    curve((-0.089,-0.025),(-0.07,0.011),(-0.006,0.027),(0.025,0.002))
    curve((0.025,0.002),(-0.011,-0.098),(-0.09,-0.091),(-0.089,-0.025))
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 0, 0)
    curve((-0.089, -0.025), (-0.07, 0.011), (-0.006, 0.027), (0.025, 0.002))
    curve((0.025, 0.002), (-0.011, -0.098), (-0.09, -0.091), (-0.089, -0.025))
    glEnd()

#mustach :D
    glBegin(GL_LINES)
    glVertex(0.253, -0.0775)
    glVertex(0.2323, -0.0163)
    glVertex(0.1924, -0.1163)
    glVertex(0.1706, -0.035)
    glVertex(0.1138, -0.132)
    glVertex(0.096, -0.0503)
    glVertex(-0.219, 0.044)
    glVertex(-0.293, -0.0028)
    glVertex(-0.319, 0.072)
    glVertex(-0.2435, 0.107)
    glEnd()
    glLineWidth(4.0)
    glBegin(GL_LINES)
    glVertex(0.041, 0.362)
    glVertex(-0.019, 0.364)
    glVertex(0.213,0.294)
    glVertex(0.28, 0.239)
    glEnd()
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Lab2 - Circle Program")
glutDisplayFunc(draw)
glutMainLoop()
