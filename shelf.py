import pygame

class Shelf:
    def __init__(self, screen, cell, we, ns, kierunek, rodzaj):
        self.kierunek = kierunek
        self.rodzaj = rodzaj
        self.cell = cell
        self.ns = ns
        self.we = we
        self.screen = screen
        self.occupied = False
        self.box = False
        if (rodzaj==1):
            self.image = pygame.image.load(r'images/kr.png')
        elif (rodzaj==2):
            self.image = pygame.image.load(r'images/la.png')
        elif (rodzaj==3):
            self.image = pygame.image.load(r'images/ra.png')
        elif (rodzaj==4):
            self.image = pygame.image.load(r'images/ni.png')
        else:
            self.image = pygame.image.load(r'images/in.png')
        self.image = pygame.transform.scale(self.image, (cell, cell))
        if (kierunek==1):
            self.image = pygame.transform.rotate(self.image, 180)
        elif (kierunek==2):
            self.image = pygame.transform.rotate(self.image, 270)
        elif (kierunek==3):
            self.image = pygame.transform.rotate(self.image, 90)
    def isOccupied(self):
        return self.occupied
    def put(self, boxik):
        self.occupied = True
        self.box = boxik
        if (self.rodzaj==1):
            self.image = pygame.image.load(r'images/krp.png')
        elif (self.rodzaj==2):
            self.image = pygame.image.load(r'images/lap.png')
        elif (self.rodzaj==3):
            self.image = pygame.image.load(r'images/rap.png')
        elif (self.rodzaj==4):
            self.image = pygame.image.load(r'images/nip.png')
        else:
            self.image = pygame.image.load(r'images/inp.png')
        self.image = pygame.transform.scale(self.image, (self.cell, self.cell))
        if (self.kierunek==1):
            self.image = pygame.transform.rotate(self.image, 180)
        elif (self.kierunek==2):
            self.image = pygame.transform.rotate(self.image, 270)
        elif (self.kierunek==3):
            self.image = pygame.transform.rotate(self.image, 90)
    def get(self):
        self.occupied = False
        if (self.rodzaj==1):
            self.image = pygame.image.load(r'images/kr.png')
        elif (self.rodzaj==2):
            self.image = pygame.image.load(r'images/la.png')
        elif (self.rodzaj==3):
            self.image = pygame.image.load(r'images/ra.png')
        elif (self.rodzaj==4):
            self.image = pygame.image.load(r'images/ni.png')
        else:
            self.image = pygame.image.load(r'images/in.png')
        self.image = pygame.transform.scale(self.image, (self.cell, self.cell))
        if (self.kierunek==1):
            self.image = pygame.transform.rotate(self.image, 180)
        elif (self.kierunek==2):
            self.image = pygame.transform.rotate(self.image, 270)
        elif (self.kierunek==3):
            self.image = pygame.transform.rotate(self.image, 90)
        return self.box
    def draw(self):
        self.screen.blit(self.image, (self.cell*self.ns, self.cell*self.we))