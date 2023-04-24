import sys
import os

try:
    import pygame
except:
    os.system('python -m pip install pygame')
    
pygame.init()
D = pygame.display.set_mode((800,600))
pygame.display.set_caption('X=0,Y=0,B=4')

BLACK = pygame.color.THECOLORS['black']

D.fill(pygame.color.THECOLORS['white'])
x = 0;y = 0;s=4
r = 798;t = 0

while True:
    for e in pygame.event.get():
        try:
            if e.dict['unicode'] == 'q':
                pygame.quit()
                sys.exit()
            if e.dict['unicode'] == 'r':
                D.fill(pygame.color.THECOLORS['white'])
                x =0 ; y = 0
                r =798 ; t = 0
            if e.dict['unicode'] == 'd':
                x += 0;y += 1
                t += 1 
                pygame.draw.line(D, BLACK,(x, y),(x, y), s)
                pygame.draw.line(D, BLACK,(r, t),(r, t), s)
            if e.dict['unicode'] == 'f':
                x += 1;y += 0
                r -= 1
                pygame.draw.line(D, BLACK,(x, y),(x, y), s)
                pygame.draw.line(D, BLACK,(r, t),(r, t), s)
            if e.dict['unicode'] == 's':
                x += -1;y += 0
                r += 1
                pygame.draw.line(D, BLACK,(x, y),(x, y), s)
                pygame.draw.line(D, BLACK,(r, t),(r, t), s)
            if e.dict['unicode'] == 'e':
                x += 0;y += -1
                t -= 1
                pygame.draw.line(D, BLACK,(x, y),(x, y), s)
                pygame.draw.line(D, BLACK,(r, t),(r, t), s)
            if e.dict['unicode'] == 'c':
                s += 1
                pygame.draw.line(D, BLACK,(x, y),(x, y), s)
            if e.dict['unicode'] == 'v':
                s -= 1
                pygame.draw.line(D, BLACK,(x, y),(x, y), s)
        except:
            pass
        pygame.display.update()
