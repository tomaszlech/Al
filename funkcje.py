from unboxOnTheFloor import UnboxOnTheFloor
from box import Box
from AStar import AStar
import random
from easygui import *
import matplotlib.pyplot as plt
from Data import Data



def zbierzBox(gen,data, moves, kordStartowy):
    regalKordy = gen.kordy
    star = AStar()
    mapForAStar = data.astarMap[:]
    mapForAStar[regalKordy[0]][regalKordy[1]] = 0
    path = star.search([kordStartowy[0], kordStartowy[1]], regalKordy, mapForAStar, 1, 1)
    cns = kordStartowy[0]
    cwe = kordStartowy[1]
    value = path[cns][cwe]

    while True:
        if cns > 0 and path[cns - 1][cwe] == (value + 1):
            cns = cns - 1
            moves.append(1)
            value = value + 1
            continue
        if cns < (len(mapForAStar) - 1) and path[cns + 1][cwe] == (value + 1):
            cns = cns + 1
            moves.append(2)
            value = value + 1
            continue
        if cwe > 0 and path[cns][cwe - 1] == (value + 1):
            cwe = cwe - 1
            moves.append(3)
            value = value + 1
            continue
        if cwe < (len(mapForAStar[0]) - 1) and path[cns][cwe + 1] == (value + 1):
            cwe = cwe + 1
            moves.append(4)
            value = value + 1
            continue
        break
    mapForAStar[regalKordy[0]][regalKordy[1]] = 1
    # wyszukiwanie ścieżki z miejsca podjęcia paczki do regału
    # zmienna path posiada macierz oraz kroki podjęte przez wózek
    path = star.search([regalKordy[0], regalKordy[1]], gen.kordyUnboxa, mapForAStar, 1, 1)
    #mapForAStar[where[0]][where[1]] = 1
    value = path[cns][cwe]
    while True:
        if(value == 0):
            if(path[cns - 1][cwe] == 1):
                cns = cns - 1
            elif(path[cns + 1][cwe] == 1):
                cns = cns + 1
            elif(path[cns][cwe - 1] == 1):
                cwe = cwe - 1
            elif(path[cns][cwe + 1] ==  1):
                cwe = cwe + 1
            value = path[cns][cwe]
            continue
        if cns > 0 and path[cns - 1][cwe] == (value + 1):
            cns = cns - 1
            moves.append(1)
            value = value + 1
            continue
        if cns < (len(mapForAStar) - 1) and path[cns + 1][cwe] == (value + 1):
            cns = cns + 1
            moves.append(2)
            value = value + 1
            continue
        if cwe > 0 and path[cns][cwe - 1] == (value + 1):
            cwe = cwe - 1
            moves.append(3)
            value = value + 1
            continue
        if cwe < (len(mapForAStar[0]) - 1) and path[cns][cwe + 1] == (value + 1):
            cwe = cwe + 1
            moves.append(4)
            value = value + 1
            continue
        break




def znajdzUnbox(data,mapa):
    unboxy = []
    iterator = 0
    ostatniWiersz = len(mapa) -1
    for x in mapa[ostatniWiersz]:
        if (isinstance(x, UnboxOnTheFloor)):
            unboxy.append((ostatniWiersz, iterator))
        iterator += 1

    data.unbox = unboxy



def policzCost(mapaBoxy, poczatek, koniec):
    astar = AStar()
    koszt = astar.search(poczatek, koniec, mapaBoxy, 1, 0)
    return koszt



def wybierzUnbox(gen, jakLiczycKoszt): #funkcja ustawiajaca jaki unbox
    if(jakLiczycKoszt == 0):
        x = random.choice([gen.unbox1, gen.unbox2])
        if(x == gen.unbox1):
            y = 0
        else:
            y= 1
        return (x,y)
    elif(jakLiczycKoszt == 1):
        return (gen.unbox1,0)
    elif(jakLiczycKoszt == 2):
        return  (gen.unbox2,1)
    elif(jakLiczycKoszt == 3):
        x = min(gen.unbox1,gen.unbox2)
        if(x == gen.unbox1):
            y = 0
        else:
            y = 1
        return (x,y)

def randomBox(mapa, regals, ile):

    regals = regals
    mapa = mapa
    tupleList = []
    ileRegalow = len(regals)
    iteration = 0

    while iteration < ileRegalow and iteration < ile:
        regal = random.choice(regals)
        if regal in tupleList:
            continue
        else:
            tupleList.append(regal)
            iteration+=1

    for (i,j,x) in tupleList:
        box = Box()
        mapa[i][j].put(box)
    """
    for t in tupleList:
        listaRegalow.append((t[0],t[1]))
    data.zajeteRegaly = listaRegalow
    """
    return mapa

def znajdzBox(mapa, regals):
    zajeteRegaly = []

    for (x,y,z) in regals:
        shelf = mapa[x][y]
        tmp = shelf.occupied
        if(tmp == True):
            zajeteRegaly.append((x,y))
    return zajeteRegaly

#wybiera z populacji dwa najlepsze chromosomy



def updateMap(data, map, mapForAstar, regals):
    data.mapa = map

    znajdzUnbox(data, map)
    data.zajeteRegaly = znajdzBox(map, regals)
    data.astarMap = data.genMap(mapForAstar)






def okno():
    try:
        good = True
        fieldValues = multenterbox("Wprowadź warunki początkowe", "Start algorytmu genetycznego", ["Ile chrom. w generacji", "Wielkosc dziedziczonego fragmentu (x>0 and x<1)", "Wartosc mutacji (x>0 and x<1)", "Gdzie odwieść paczkę: (0 or 1 or 2 or 3)", "Ile generacji"])
        if(fieldValues[0] == None):
            return 0
        if(not(fieldValues[0].isnumeric() and (fieldValues[0]!=""))):
                good = False
                msgbox("Wartość nie jest liczbą", "Błąd")

        if(isinstance(float(fieldValues[1]),float) and (fieldValues[1]!="")):
            if((float(fieldValues[1])<=0) and (good==True) and (float(fieldValues[1])>= 1)):
                msgbox("Zla wartosc fragmentu")
                good = False
        elif (good == True):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False

        if(isinstance(float(fieldValues[2]),float) and (fieldValues[2]!="")):
            if((float(fieldValues[1])<=0) and (good==True) and (float(fieldValues[1])>= 1)):
                msgbox("Zla wartosc mutacji")
                good = False
        elif (good == True):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False

        if(fieldValues[3].isnumeric() and (fieldValues[3]!="")):
            if(((int(fieldValues[3]) != 0) and (int(fieldValues[3]) != 1) and (int(fieldValues[3]) != 2) and (int(fieldValues[3]) != 3))):
                msgbox("Zla wartosc unboxa")
                good = False
        elif (good == True):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False

        if(not(fieldValues[4].isnumeric() and (fieldValues[4]!=""))):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False

        if(good == True):
            return [fieldValues[0], fieldValues[1], fieldValues[2],fieldValues[3], fieldValues[4]]

    except:
        return 0



def rysujWykres(data):
    x = list(range(len(data.doWykresu)))
    y = data.doWykresu
    plt.scatter(x, y, marker= "o", color = "r")
    plt.show()
"""
data = Data()
data.doWykresu = [1,2,3]
x = list(range(1, len(data.doWykresu)+ 1))
y = data.doWykresu
rysujWykres(data,x)
print(x)
"""