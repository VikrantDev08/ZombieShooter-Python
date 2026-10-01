import os
import pygame

# Set working directory to the folder containing this script

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

win=pygame.display.set_mode((1000,700))

pygame.display.set_caption('Second Pygame')

Clock=pygame.time.Clock()

score=0
bulletsound=pygame.mixer.Sound('bullet.mp3')
hitsound=pygame.mixer.Sound('hit.mp3')
music=pygame.mixer.music.load('music.mp3')

pygame.mixer.music.play(-1)

class Player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isjump=False
        self.jumpcount=10
        self.left=False
        self.right=False
        self.walkcount=0
        self.standing=True
        self.hitbox=(self.x+17,self.y,28,60)
        self.hits=0

    def draw(self,win):
        if (self.walkcount+1)>=27:
                self.walkcount=0
        if self.right:
            win.blit(walkRight[int(self.walkcount//3)],(self.x,self.y))
            self.walkcount+=1
        elif self.left:
            win.blit(walkLeft[int(self.walkcount//3) ],(self.x,self.y))
            self.walkcount+=1
        else:
            win.blit(char,(self.x,self.y))
        self.hitbox=(self.x+17,self.y,28,60)

    def damage(self):
        self.x=500
        self.hits+=1
        print('Player Hit')
        pass
class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walkcount=0
        self.vel=5
        self.right=False
        self.left=False
        self.a=False
        self.hitbox=(self.x+17,self.y,30,60)
        self.hits=0
        self.health=10
        self.visible=True

    def draw(self,win):
        self.move()
        if self.visible:
            if (self.walkcount+1)>=33:
                self.walkcount=0
            if self.right:
                win.blit(enemy.walkRight[int(self.walkcount//3)],(self.x,self.y))
                self.walkcount+=1
            elif self.left:
                win.blit(enemy.walkLeft[int(self.walkcount//3) ],(self.x,self.y))
                self.walkcount+=1 
            pygame.draw.rect(win,(225,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,50 - ((10 -self.health)*5),10))
            self.hitbox=(self.x+17,self.y,30,60)
            pass
        

    def damage(self):
        self.hits+=1
        print('Enemy Hit')
        self.health-=1
        if self.health==0:
            self.visible=True
            self.health=10
            self.x=10
        pass

    def move(self):
        if self.a==False:
            if self.x<935:
                self.right=True
                self.left=False
                self.x+=self.vel
                    
            if self.x==935:
                self.right=False
                self.left=True
                self.a=True

        if self.a==True:
            if self.x>0:
                self.right=False
                self.left=True
                self.x-=self.vel
            if self.x==0:
                self.right=True
                self.left=False
                self.a=False   
            
class red(object):
    red1=pygame.image.load('red.png')
    red2=pygame.image.load('red2.png')
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=2
        self.isjump=False
        self.jumpcount=10
        self.left=False
        self.right=False
        self.standing=True
        self.a=False
        self.hitbox=(self.x+10,self.y+5,35,60)
        self.hits=0
        self.health=10
        self.visible=True
    def draw(self,win):
        self.move()
        if self.right:
                win.blit(self.red1,(self.x,self.y))
        elif self.left:
            win.blit(self.red2,(self.x,self.y))       
        self.hitbox=(self.x+10,self.y+5,35,60)
        pygame.draw.rect(win,(225,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
        pygame.draw.rect(win,(0,255,0),(self.hitbox[0],self.hitbox[1]-20,50 - ((10 -self.health)*5),10))
        pass

    def move(self):
        if self.a==False:
            if self.x<934:
                self.right=True
                self.left=False
                self.x+=self.vel
                        
            if self.x==934:
                self.right=False
                self.left=True
                self.a=True
    
        if self.a == True:
            if self.x>0:
                self.right=False
                self.left=True
                self.x-=self.vel
            if self.x==0:
                self.right=True
                self.left=False
                self.a=False
    def damage(self):
        self.hits+=1
        print('Red Hit')
        if self.health>0:
            self.health-=1
        else:
            self.visible=True
            self.health=10
            self.x=20
        pass

class hit(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=10*facing

    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)


walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.png')
char = pygame.image.load('standing.png')

enemy=enemy(10,550,64,64)

blaze=Player(500,550,64,64)


redchar=red(20,550,64,64)

b,c,d=True,True,True
font=pygame.font.SysFont('comicsans',30,True)

def RedrawGameWindow():
    global blaze,enemy,redchar
    win.blit(bg,(0,0))
    text=font.render('Score: '+str(score),1,(0,255,255))
    win.blit(text,(20,10))
    text2=font.render('Hits taken: '+str(blaze.hits),1,(0,255,255))
    win.blit(text2,(770,10))
    if blaze.hits<100:
        blaze.draw(win)
    if blaze.hits==100:
        print('Game Over')
    if enemy.visible:
        enemy.draw(win)
    if redchar.visible:
        redchar.draw(win)
    for bullet in bullets:
        hit.draw(bullet,win)
    pygame.display.update()


run=True
bullets=[]
shootloop=0

while run:
    Clock.tick(27)

    if shootloop>0:
        shootloop+=1
    if shootloop>9:
        shootloop=0
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    if enemy.visible==True:        
        if blaze.hitbox[0] in range (enemy.hitbox[0],enemy.hitbox[0]+enemy.hitbox[2]) and blaze.hitbox[1] in range(enemy.hitbox[1],enemy.hitbox[1]+enemy.hitbox[3]) :
                blaze.damage()
    if redchar.visible==True:
        if blaze.hitbox[0] in range (redchar.hitbox[0],redchar.hitbox[0]+redchar.hitbox[2]) and blaze.hitbox[1]+10 in range(redchar.hitbox[1],redchar.hitbox[1]+redchar.hitbox[3]):
                blaze.damage()

    for bullet in bullets:
        
        if (bullet.x in range(enemy.hitbox[0],enemy.hitbox[0]+enemy.hitbox[2]) and bullet.y in range(enemy.hitbox[1],enemy.hitbox[3]+enemy.hitbox[1])) :
                enemy.damage()
                bullets.pop(bullets.index(bullet))
                shootloop=1
                score+=1
        if (bullet.x in range(redchar.hitbox[0],redchar.hitbox[0]+redchar.hitbox[2]) and bullet.y in range(redchar.hitbox[1],redchar.hitbox[3]+redchar.hitbox[1])):
            redchar.damage()                
            bullets.pop(bullets.index(bullet))
            shootloop=1
            score+=1
        if bullet.x<1000 and bullet.x>0 :
            bullet.x+=bullet.vel
        

        else:
            bullets.pop(bullets.index(bullet))

        

    keys=pygame.key.get_pressed()

    if blaze.left:
        facing=-1
    else:
        facing=1

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletsound.play()
        if len(bullets)<6:
            bullets.append(hit(round(blaze.x+blaze.width//2),round(blaze.y+blaze.height//2),6,(25,255,89),facing))
        shootloop=1
    if keys[pygame.K_LEFT]:
        blaze.right=False
        blaze.left=True
        blaze.standing=False
        if blaze.x<=10:
            continue
        else:
            blaze.x-=blaze.vel

    elif keys[pygame.K_RIGHT]:
        blaze.right=True
        blaze.left=False
        blaze.standing=False
        if blaze.x>=926:
            continue
        else:
            blaze.x+=blaze.vel

    else:
        blaze.standing=True
        blaze.walkcount=0

    if not(blaze.isjump):
        if keys[pygame.K_UP]:
            blaze.isjump=True
            blaze.right=False
            blaze.left=False
            blaze.walkcount=0
    else:

        if blaze.jumpcount>=-10:
            neg=1
            if blaze.jumpcount<0:
                neg=-1
            blaze.y-=blaze.jumpcount**2*0.5*neg
            blaze.jumpcount-=1

        else:
            blaze.isjump=False
            blaze.jumpcount=10

    RedrawGameWindow()
    
pygame.quit()





