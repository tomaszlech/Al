import pygame

class Wall:
    def __init__(self, screen, cell, we, ns):
        self.cell = cell
        self.ns = ns
        self.we = we
        self.screen = screen
        self.image = pygame.image.load(r'images/sc.png')
        self.image = pygame.transform.scale(self.image, (cell, cell))
    def draw(self):
        self.screen.blit(self.image, (self.cell*self.ns, self.cell*self.we))