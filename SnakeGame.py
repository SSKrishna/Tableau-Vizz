#snake game

#our game imports
import pygame,sys,random,time
check_errors=pygame.init()
if check_errors[1]>0:
    print("(!) Had {0} initializing errors,existing...".format(check_errors[1]))
    exit(-1)
else:
    print ("Pygame Successfully Intialized!")
#Play Surface
playSurface= pygame.display.set_mode((720,460)) #display screen
pygame.display.set_caption('snake game!')  #display caption
time.sleep(5)  # timer for displaying game
#colors
red=pygame.Color(255,0,0) #game over
green=pygame.Color(0,255,0) #snake
black=pygame.Color(0,0,0) #score
white=pygame.Color(255,255,255) #back ground
brown=pygame.Color(165,42,42) #food

#FPS(frames per second) Controller
fpsController=pygame.time.Clock()

#Important variables
snakePos=[100,50] #Snake Position
snakeBody=[[100,50],[90,50],[80,50]] #Snake Length
foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10] #Food Position
foodSpawn= True

direction= "RIGHT"
changeto= direction

#Game Over Function
def gameOver(): #defining Gameover function
    myFont= pygame.font.SysFont('monaco',72)
    Gosurf= myFont.render('Game Over!',True, red)
    GOrect=Gosurf.get_rect()
    GOrect.midtop=(360,15)
    playSurface.blit(Gosurf,GOrect)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit() #pygame exit
    sys.exit()  #console exit
while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT or event.key==ord('d'):
                changeto="RIGHT"
            if event.key==pygame.K_LEFT or event.key==ord('a'):
                changeto="LEFT"
            if event.key==pygame.K_UP or event.key==ord('w'):
                changeto="UP"
            if event.key==pygame.K_DOWN or event.key==ord('s'):
                changeto="DOWN"
            if event.key== pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
    #Validation of Direction
    if changeto=="RIGHT" and not direction=="LEFT":
        direction=="RIGHT"
    if changeto=="LEFT" and not direction=="RIGHT":
        direction=="LEFT"
    if changeto=="UP" and not direction=="DOWN":
        direction=="UP"
    if changeto=="DOWN" and not direction=="UP":
        direction=="DOWN"
    if direction=='RIGHT':
        snakePos[0] +=10
    if direction=='LEFT':
        snakePos[0] -=10
    if direction=='UP':
        snakePos[1] -=10
    if direction=='DOWN':
        snakePos[1] +=10
    
    #Snake body mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
        foodSpawn= False
    else:
        snakeBody.pop()
    #food Spawn
    if foodSpawn==False:
        foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn= True
    playSurface.fill(white)
    
    pygame.display.flip()
    
    
    
    
    

    
