import pygame
from random import randint
pygame.init()
WIDTH, HEIGTH =400,600
screen= pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("Flappy Bird")
clock=pygame.time.Clock()
GREEN= (0,200,0)
BLUE=(0, 0, 255)
RED=(255,0,0)
BLACK=(0,0,0)
YELLOW=(255,255,0)
TUBE_WIDTH=50
tube1_heigth=randint(100,400)
tube2_heigth=randint(100,400)
tube3_heigth=randint(100,400)
TUBE_GAP=150
tube1_x=600
tube2_x=800
tube3_x=1000
tube_y=0
bird_x=100
bird_y=200
BIRD_WIGTH=35
BIRD_HEIGTH=35
GRAVITY=0.5
bird_drop=0
score=0
font=pygame.font.SysFont('sans', 20)
slowmove=2
score_check1=False
score_check2=False
score_check3=False
running = True          
resetgame=False
back_ground=pygame.image.load("background.png")
back_ground=pygame.transform.scale(back_ground,(WIDTH,HEIGTH))
bird_ground=pygame.image.load("bird.png")
bird_ground=pygame.transform.scale(bird_ground,(BIRD_WIGTH,BIRD_HEIGTH))
while running:
    clock.tick(60)
    screen.fill(GREEN)
    screen.blit(back_ground,(0,0))
 
    # generate tube
    tube1_rect=pygame.draw.rect(screen,BLUE,(tube1_x,tube_y,TUBE_WIDTH,tube1_heigth))

    tube2_rect=pygame.draw.rect(screen,BLUE,(tube2_x,tube_y,TUBE_WIDTH,tube2_heigth))

    tube3_rect=pygame.draw.rect(screen,BLUE,(tube3_x,tube_y,TUBE_WIDTH,tube3_heigth))

    # generate opposite tube
    tubeop1_rect=pygame.draw.rect(screen,BLUE,(tube1_x,tube1_heigth+TUBE_GAP,TUBE_WIDTH,HEIGTH-tube1_heigth-TUBE_GAP))

    tubeop2_rect=pygame.draw.rect(screen,BLUE,(tube2_x,tube2_heigth+TUBE_GAP,TUBE_WIDTH,HEIGTH- TUBE_GAP- tube2_heigth))

    tubeop3_rect=pygame.draw.rect(screen,BLUE,(tube3_x,tube3_heigth+TUBE_GAP,TUBE_WIDTH,HEIGTH- TUBE_GAP- tube3_heigth))

    if tube1_x<-TUBE_WIDTH:
        tube1_x=550
        tube1_heigth=randint(100,400)
        score_check1=False
    if tube2_x<-TUBE_WIDTH:
        tube2_x=550
        tube2_heigth=randint(100,400)
        score_check2=False
    if tube3_x<-TUBE_WIDTH:
        tube3_x=550
        tube3_heigth=randint(100,400)
        score_check3=False
    tube1_x-=slowmove
    tube2_x-=slowmove 
    tube3_x-=slowmove
    if slowmove < 10:
        slowmove+=0.0015

    # GENERATE BIRD 
    # bird_rect=pygame.draw.rect(screen,RED,(bird_x,bird_y,BIRD_WIGTH,BIRD_HEIGTH))
    bird_rect=screen.blit(bird_ground,(bird_x,bird_y))
    bird_y+= bird_drop
    bird_drop+=GRAVITY

    # SCORE
    score_txt=font.render("Score:" + str(score), True, BLACK)
    screen.blit(score_txt,(5,5))
    if tube1_x + TUBE_WIDTH <= bird_x and score_check1==False:
        score+=1
        score_check1=True
    if tube2_x + TUBE_WIDTH <= bird_x and score_check2==False:
        score+=1
        score_check2=True
    if tube3_x + TUBE_WIDTH <= bird_x and score_check3== False:
        score+=1
        score_check3=True

    # stop screen   
    glass=pygame.draw.rect(screen, YELLOW,(0,550,WIDTH,HEIGTH))
    for tube in [tube1_rect,tube2_rect,tube3_rect,tubeop1_rect,tubeop2_rect,tubeop3_rect,glass]:
        if bird_rect.colliderect(tube):
            slowmove=0
            bird_drop=0
            resetgame=True
            gameover_txt=font.render("Game over, Score:" + str(score), True,BLACK)
            screen.blit(gameover_txt, (100,250))
            press_txt=font.render("Press space to continue: ", True,BLACK)
            screen.blit(press_txt,(100,300))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #reset 
                if resetgame==True:
                    bird_y=200
                    slowmove=2
                    tube1_x=600
                    tube2_x=800
                    tube3_x=1000
                    score=0
                    resetgame=False
                else:
                    bird_drop=0
                    bird_drop-=8
    pygame.display.flip()

   
pygame.quit()
