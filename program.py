import pygame
from os import sys
from generate import  Generate
from floor import Floor
from wall import Wall
from shelf import Shelf
from wheel import Wheel
from boxOnTheFloor import BoxOnTheFloor
from box import Box
from unboxOnTheFloor import UnboxOnTheFloor
from AStar import AStar
import numpy
import easygui
from neurons import Neurons
from whereDecision import WhereDecision
from Evencik import Evencik
import pathlib
from Data import Data
from genetyczne import *

class MainWindow:
    def __init__(self, szerokosc, wysokosc, kruche, latwopalne, radioaktywne, niebezpieczne):
        #config
        self.cell = 50
        #init
        pygame.init()
        pygame.display.set_caption('Inteligentny wózek widłowy')
        self.clock = pygame.time.Clock()
        self.ticks = 0
        self.data = Data()
        self.moves = []
        self.regals = []
        self.map = Generate.generate(szerokosc+2, wysokosc+2, kruche, latwopalne, radioaktywne, niebezpieczne)
        self.mapForAStar = Generate.generate(szerokosc+2, wysokosc+2, kruche, latwopalne, radioaktywne, niebezpieczne)
        self.screen = pygame.display.set_mode((((szerokosc+2)*self.cell), ((wysokosc+2)*self.cell)))
        self.neurons = Neurons()
        self.whereDecision = WhereDecision()
        #create
        self.wheel = Wheel(self.screen, self.cell);
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if (self.map[i][j]==1):
                    self.map[i][j] = Wall(self.screen, self.cell, i, j)
                    self.mapForAStar[i][j] = 1
                elif (self.map[i][j]==2):
                    self.map[i][j] = Floor(self.screen, self.cell, i, j)
                    self.mapForAStar[i][j] = 0
                elif (self.map[i][j]==23):
                    self.map[i][j] = UnboxOnTheFloor(self.screen, self.cell, i, j)
                    self.mapForAStar[i][j] = 0

                else:
                    #regals (kordy i,j oraz rodzaj regału)
                    self.regals.append((i, j, (self.map[i][j]-3)//4))
                    self.map[i][j] = Shelf(self.screen, self.cell, i, j, (self.map[i][j]-3)%4, (self.map[i][j]-3)//4)
                    self.mapForAStar[i][j] = 1






        #################################################
#loop
        while True:
            self.events()
            self.draw()
            self.clock.tick(40)
            self.ticks+=1
            if self.ticks>10:
                self.ticks=0
                if len(self.moves)>0:
                    if(self.moves[0]==1):
                        self.wheel.move(Evencik(pygame.K_UP), self.map)
                    elif (self.moves[0]==2):
                        self.wheel.move(Evencik(pygame.K_DOWN), self.map)
                    elif (self.moves[0]==3):
                        self.wheel.move(Evencik(pygame.K_LEFT), self.map)
                    elif (self.moves[0]==4):
                        self.wheel.move(Evencik(pygame.K_RIGHT), self.map)

                    self.moves.pop(0)

    def events(self):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                sys.exit()

            elif(event.type==pygame.KEYDOWN):
                if event.key == pygame.K_g:
                    updateMap(self.data, self.map, self.mapForAStar, self.regals)

                    dane = okno()
                    if(dane == 0):
                        continue

                    start(self.data,self.wheel, dane)
                    for gen in self.data.best[0]:
                        if(gen.unboxWczesniejszegoGenu == None):
                            kordStartowy = (self.wheel.ns, self.wheel.we)
                        else:
                            kordStartowy = self.data.unbox[gen.unboxWczesniejszegoGenu]

                        zbierzBox(gen,self.data, self.moves, kordStartowy)
                    self.data.__init__()
                elif(event.key== pygame.K_r):
                    self.map = randomBox(self.map, self.regals, 2)
                    updateMap(self.data, self.map, self.mapForAStar, self.regals)
                elif len(self.moves)==0:
                    self.wheel.move(event, self.map)

            elif(event.type==pygame.MOUSEBUTTONDOWN):
                if (type(self.map[0][2]) == Floor):
                    meh = easygui.fileopenbox("Wybierz zdjęcie paczki", "Wybierz zdjęcie paczki", filetypes = [["*.jpg", "*.jpeg", "*.png", "Pliki graficzne"]])
                    if meh is None:
                        return
                    while pathlib.Path(meh).suffix!=".jpg" and pathlib.Path(meh).suffix!=".jpeg" and pathlib.Path(meh).suffix!=".png":
                        meh = easygui.fileopenbox("Wybierz zdjęcie paczki", "Wybierz zdjęcie paczki", filetypes = [["*.jpg", "*.jpeg", "*.png", "Pliki graficzne"]])
                        if meh is None:
                            return
                    whatIsIt = self.neurons.whatIsIt(meh)
                    where = self.whereDecision.recognize(whatIsIt, self.regalsik())
                    self.map[0][2] = BoxOnTheFloor(self.screen, self.cell, 0, 2, Box())

                    star = AStar()
                    path = star.search([self.wheel.ns, self.wheel.we], [0, 2], self.mapForAStar, 1, 1)
                    cns = self.wheel.ns
                    cwe = self.wheel.we
                    value = path[cns][cwe]
                    while True:
                        if cns>0 and path[cns-1][cwe]==(value+1):
                            cns=cns-1
                            self.moves.append(1)
                            value=value+1
                            continue
                        if cns<(len(self.mapForAStar)-1) and path[cns+1][cwe]==(value+1):
                            cns=cns+1
                            self.moves.append(2)
                            value=value+1
                            continue
                        if cwe>0 and path[cns][cwe-1]==(value+1):
                            cwe=cwe-1
                            self.moves.append(3)
                            value=value+1
                            continue
                        if cwe<(len(self.mapForAStar[0])-1) and path[cns][cwe+1]==(value+1):
                            cns=cns+1
                            self.moves.append(4)
                            value=value+1
                            continue
                        break
                    self.mapForAStar[where[0]][where[1]] = 0
                    # wyszukiwanie ścieżki z miejsca podjęcia paczki do regału
                    # zmienna path posiada macierz oraz kroki podjęte przez wózek
                    path = star.search([0, 2], where, self.mapForAStar, 1, 1)
                    self.mapForAStar[where[0]][where[1]] = 1
                    value = path[cns][cwe]
                    while True:
                        if cns>0 and path[cns-1][cwe]==(value+1):
                            cns=cns-1
                            self.moves.append(1)
                            value=value+1
                            continue
                        if cns<(len(self.mapForAStar)-1) and path[cns+1][cwe]==(value+1):
                            cns=cns+1
                            self.moves.append(2)
                            value=value+1
                            continue
                        if cwe>0 and path[cns][cwe-1]==(value+1):
                            cwe=cwe-1
                            self.moves.append(3)
                            value=value+1
                            continue
                        if cwe<(len(self.mapForAStar[0])-1) and path[cns][cwe+1]==(value+1):
                            cwe=cwe+1
                            self.moves.append(4)
                            value=value+1
                            continue
                        break
                    self.data.zajeteRegaly = znajdzBox(self.map, self.regals)

    def draw(self):
        self.screen.fill((33,69,108))
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                self.map[i][j].draw()
        self.wheel.draw()
        pygame.display.flip()
    def regalsik(self):
        tmp = []
        for regal in self.regals:
            if self.map[regal[0]][regal[1]].isOccupied()==False:
                tmp.append(regal)
        return tmp
