import pygame
import random as rd

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 700))

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LSALMON = (255, 160, 122)
PEACH = (255, 218, 185)
LEMONE = (255, 250, 205)
SKYBLUE = (100, 149, 237)
TOMATO = (255, 99, 71)
CADET = (176, 196, 222)
SLATE = (106, 90, 205)
DARK = (72, 61, 109)
BROWN = (139, 69, 19)

def draw_bird(x, y, a):
    #x,y-the size of the image, a-relative bird sizes
    pygame.draw.arc(screen, BROWN, (x, y, 60*a, 40*a), 0.5, 2,5)
    pygame.draw.arc(screen, BROWN, (x + 50*a, y - 2*a, 60*a, 30*a), 1.6, 3,5)
    pygame.draw.lines(screen, BROWN, False, [[x + 23*a, y + 3*a],
                                             [x + 52*a, y + 12*a],[x + 78*a, y - a]], 6)

x, y = 640, 480 #The size of the screen
screen = pygame.display.set_mode([x, y])
pygame.display.set_caption('Refactored by Ilyas')

# The colours of background
for n in range (0, 288, 2):
    pygame.draw.rect(screen, (255, 154+n/3, 116+n/3), (0, n, x, 2))
pygame.draw.rect(screen, SKYBLUE, (0, 3*y/5, x, 2*y/5))

# The sun
pygame.draw.circle(screen, TOMATO, [int(x/2),int(y/5)],40)

#Preparations for mountains far away
M = list()
M.append((0, y/6))
for n in range (1, 9, 1):
    M.append((n*x/10, y/12+rd.randint(-y/15, y/15)))
M.append((1.05*x, y/6))
M.append((0, y/6))

# Mountains far away.
mount1 = pygame.Surface((1.05*x, y/6))
mount1.fill(TOMATO)
mount1.set_colorkey(TOMATO)
pygame.draw.polygon(mount1, CADET, M)
screen.blit(pygame.transform.rotate(mount1, 6), (-12, y/5))

#Preparations for mountains in the middle
L = list()
L.append((0, y/4))
for n in range (1, 9, 1):
    L.append((n*x/10, y/10+rd.randint(-y/10, y/10)))
L.append((1.05*x, y/4))
L.append((0, y/4))

# Mountains in the middle
mount2 = pygame.Surface((x, y/4))
mount2.fill(TOMATO)
mount2.set_colorkey(TOMATO)
pygame.draw.polygon(mount2, SLATE, L)
screen.blit(pygame.transform.rotate(mount2, 0), (0, 5*y/14))

#Preparations for mountains in front of us
N = list()
N.append((0, y/3))
for n in range (1, 9, 1):
    N.append((n*x/10, y/6+rd.randint(-y/6, y/6)))
N.append((1.05*x, y/3))
N.append((0, y/3))

# Mountains in front of us
mount3 = pygame.Surface((x, y/3))
mount3.fill(TOMATO)
mount3.set_colorkey(TOMATO)
pygame.draw.polygon(mount3, DARK, N)
screen.blit(pygame.transform.rotate(mount3, 0), (0, 8*y/12))
pygame.draw.polygon(screen, DARK, [(0, y), (0, 7*y/13), (x/8, 7*y/13+50), (x/7, y)])
pygame.draw.polygon(screen, DARK, [(5*x/8, y), (6*x/7, 7*y/13+50), (x, 7*y/13), (x, y)])

# Birds
birds=[(300*x/640, 280*y/480, 1), (430*x/640, 360*y/480, 1),
       (350*x/640, 330*y/480, 0.7), (400*x/640, 315*y/480, 0.7),
       (320*x/640, 160*y/480, 0.5), (290*x/640, 140*y/480, 0.5),
       (270*x/640, 170*y/480, 0.5), (260*x/640, 220*y/480, 0.5)]

for i, j, k in birds: draw_bird(i, j, k)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()