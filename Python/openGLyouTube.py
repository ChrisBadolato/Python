import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
    )
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1,),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1,)
    
    )


def Cube():
    glBegin(GL_QUADS) #doing the surface of the square
    
    for surface in surfaces: #for each surface
        x = 0
         #changes the color of the edges
        for vertex in surface: #for each vertices
            x+=1
            glVertex3fv(verticies[vertex])
            glColor3fv(colors[x])
        
    glEnd()
    
    glBegin(GL_LINES) #draws the outside lines of the square
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), .1, 50)

    glTranslatef(0.0,0.0, -5) # we can shift the object left or right or z direction

    glRotatef(25,2,1,0) #start rotation


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0.0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                    
            if event.type == pygame.MOUSEBUTTONDOWN: #means wheel is moving forward
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)
                
        #glRotatef(1,3,1,1)  #will keep the cube rotating      
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
            
    
