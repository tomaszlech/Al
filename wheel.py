import pygame
from floor import Floor
from boxOnTheFloor import BoxOnTheFloor
from unboxOnTheFloor import UnboxOnTheFloor
from shelf import Shelf

class Wheel:
    def __init__(self, screen, cell):
        self.cell = cell
        #kordy wozka
        self.ns = 1
        self.we = 2
        self.direction = 3
        self.m_ns = 0
        self.m_we = 0
        self.occupied = False
        self.box = False
        # 1 - w gore
        # 2 - w prawo
        # 3 - w dol
        # 4 - w lewo
        self.screen = screen
        self.imageorg = pygame.image.load(r'images/wo.png')
        self.imageorg = pygame.transform.scale(self.imageorg, (cell, cell))
        self.image = pygame.transform.scale(self.imageorg, (cell, cell))
    def draw(self):
        self.screen.blit(self.image, ((self.cell*self.we)+self.m_we, (self.cell*self.ns)+self.m_ns))
        self.m_ns = self.m_ns*(0.9)
        self.m_we = self.m_we*(0.9)
    def isOccupied(self):
        return self.occupied
    def putBox(self, boxik):
        self.box = boxik
        self.occupied = True
        self.imageorg = pygame.image.load(r'images/wop.png')
        self.imageorg = pygame.transform.scale(self.imageorg, (self.cell, self.cell))
        self.image = pygame.transform.scale(self.imageorg, (self.cell, self.cell))
    def getBox(self):
        self.occupied = False
        self.imageorg = pygame.image.load(r'images/wo.png')
        self.imageorg = pygame.transform.scale(self.imageorg, (self.cell, self.cell))
        self.image = pygame.transform.scale(self.imageorg, (self.cell, self.cell))
        return self.box
    def move(self, move, krata):
        if(move.key==pygame.K_DOWN):
            if(type(krata[self.ns][self.we])==UnboxOnTheFloor):
                pass
            elif(type(krata[self.ns+1][self.we])==Floor):
                self.ns+=1
                self.m_ns=self.cell*(-1)
                self.direction = 3
            elif(type(krata[self.ns+1][self.we])==Shelf):
                if(self.occupied==True and krata[self.ns+1][self.we].isOccupied()==False and krata[self.ns+1][self.we].kierunek==1):
                    krata[self.ns+1][self.we].put(self.getBox())
                    self.direction = 3
                elif(self.occupied==False and krata[self.ns+1][self.we].isOccupied()==True and krata[self.ns+1][self.we].kierunek==1):
                    self.putBox(krata[self.ns+1][self.we].get())
                    self.direction = 3
            elif(type(krata[self.ns+1][self.we])==UnboxOnTheFloor):     # Aktywacja unBoxOnTheFloor jak wózek najedzie na pole przed nim
                if(self.ns+1==len(krata)-1):
                    self.ns+=1
                    self.m_ns=self.cell*(-1)
                    self.direction = 1
                    self.getBox()
        elif(move.key==pygame.K_UP):
            if(type(krata[self.ns-1][self.we])==Floor):
                self.ns-=1
                self.m_ns=self.cell
                self.direction = 1
            elif(type(krata[self.ns-1][self.we])==BoxOnTheFloor):
                if(self.occupied==False):
                    self.putBox(krata[self.ns - 1][self.we].get())
                    krata[self.ns - 1][self.we] = Floor(self.screen, self.cell, self.ns - 1, self.we)
                    self.ns -= 1
                    self.m_ns = self.cell
                    self.direction = 1
            elif(type(krata[self.ns-1][self.we])==Shelf):
                if(self.occupied==True and krata[self.ns-1][self.we].isOccupied()==False and krata[self.ns-1][self.we].kierunek==0):
                    krata[self.ns-1][self.we].put(self.getBox())
                    self.direction = 1
                elif(self.occupied==False and krata[self.ns-1][self.we].isOccupied()==True and krata[self.ns-1][self.we].kierunek==0):
                    self.putBox(krata[self.ns-1][self.we].get())
                    self.direction = 1
        elif(move.key==pygame.K_LEFT):
            if(type(krata[self.ns][self.we-1])==Floor):
                self.we-=1
                self.m_we=self.cell
                self.direction = 4
            elif(type(krata[self.ns][self.we-1])==Shelf):
                if(self.occupied==True and krata[self.ns][self.we-1].isOccupied()==False and krata[self.ns][self.we-1].kierunek==3):
                    krata[self.ns][self.we-1].put(self.getBox())
                    self.direction = 4
                elif(self.occupied==False and krata[self.ns][self.we-1].isOccupied()==True and krata[self.ns][self.we-1].kierunek==3):
                    self.putBox(krata[self.ns][self.we-1].get())
                    self.direction = 4
        elif(move.key==pygame.K_RIGHT):
            if(type(krata[self.ns][self.we+1])==Floor):
                self.we+=1
                self.m_we=self.cell*(-1)
                self.direction = 2
            elif(type(krata[self.ns][self.we+1])==Shelf):
                if(self.occupied==True and krata[self.ns][self.we+1].isOccupied()==False and krata[self.ns][self.we+1].kierunek==2):
                    krata[self.ns][self.we+1].put(self.getBox())
                    self.direction = 2
                elif(self.occupied==False and krata[self.ns][self.we+1].isOccupied()==True and krata[self.ns][self.we+1].kierunek==2):
                    self.putBox(krata[self.ns][self.we+1].get())
                    self.direction = 2
        if (self.direction==1):
            self.image = pygame.transform.rotate(self.imageorg, 180)
        elif (self.direction==2):
            self.image = pygame.transform.rotate(self.imageorg, 90)
        elif (self.direction==3):
            self.image = pygame.transform.rotate(self.imageorg, 0)
        elif (self.direction==4):
            self.image = pygame.transform.rotate(self.imageorg, 270)
