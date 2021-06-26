import pygame

class BoxOnTheFloor:
    def __init__(self, screen, cell, we, ns, box):
        self.cell = cell
        self.ns = ns
        self.occupied = True
        self.box = box
        self.we = we
        self.screen = screen
        self.image = pygame.image.load(r'images/pa.png')
        self.image = pygame.transform.scale(self.image, (cell, cell))
    def get(self):
        return self.box
    def draw(self):
        self.screen.blit(self.image, (self.cell*self.ns, self.cell*self.we))