from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
 
window = 0                                             # glut window number
width, height = 500, 700
# window size
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("titittes.com")              # create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()   
      
 
def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                   # reset position# ToDo draw rectangle  
    glutSwapBuffers()
    # important for double buffering  
    
def init_display_list():
    glNewList(list_number,GL_COMPILE)
    glPushMatarix()
    glTranslatef(0.,1.,-1.)#move where you want to put the object
    glutSolidSphere(1.,5.,5.)
    glPopMatrix()
    glEndList()
    return
     
def display():
     glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
     glCallList(list_number)
     glutSwapBuffers()
     return

 
  
