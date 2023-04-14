import pygame
import time


pygame.init()


WIDTH,HEIGHT = (400,400)
img = pygame.image.load("ssd.png")
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
ico = pygame.display.set_icon(img)



color_BLACK = (1,1,1)
color_green = (0,255,0)
color_red = (255,0,0)

def TEXT(T,x,y,s):
    font = pygame.font.Font("freesansbold.ttf",s)
    text = font.render(T,True,color_BLACK)
    SCREEN.blit(text,(x,y))


def show_img(x,y):
    file = "HART.jpg"
    IMG = pygame.transform.scale(pygame.image.load(file),(100,100))
    SCREEN.blit(IMG,(x,y))

def YES():
    global run
    run = True
    path = True
    while path:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        SCREEN.fill((255,255,255))
        font = pygame.font.Font("freesansbold.ttf",35)
        text = font.render("Thanks Bro",True,(0,0,0))
        SCREEN.blit(text,(95,60))
        show_img(150,200)
        pygame.display.update()
        time.sleep(2)
        quit()

def Button(x,y,w,h,color1,color2,activate=None):
    mouse = pygame.mouse.get_pos()
    if mouse[0] > x and mouse[0] < x+w and mouse[1] > y and mouse[1] < y+h:
        pygame.draw.rect(SCREEN,color2,(x+70,y,w,h))
        TEXT("No",x+85,y+4,18)
    else:
        pygame.draw.rect(SCREEN,color2,(x,y,w,h))
        TEXT("No",x+15,y+4,18)

def Button2(x,y,w,h,color1,color2,activate=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if mouse[0] > x and mouse[0] < x+w and mouse[1] > y and mouse[1] < y+h:
        pygame.draw.rect(SCREEN,color1,(x,y,w,h))
        if click[0] == True:
            activate()
    else:
        pygame.draw.rect(SCREEN,color2,(x,y,w,h))

run = False  
while not run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
    SCREEN.fill((255,255,255))

    TEXT("Are you gay?",95,60,35)

    

    Button(100,190,60,30,color_green,color_red)
    Button2(250,190,60,30,color_green,color_red,YES)
    TEXT("Yes",265,195,18)
    
    pygame.display.update()


