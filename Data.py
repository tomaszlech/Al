


class Data:

    def __init__(self):
        self.zajeteRegaly = [] #krotka (x,y)
        self.mapa = []
        self.unbox = []
        self.astarMap = []
        self.geny = []
        self.kordyWozka = None
        self.jakLiczycKoszt = None
        self.best = None
        self.histZmian = []
        self.doWykresu = []

    def genMap(self, mapa):
        tmpMap = mapa.copy()
        for regal in self.zajeteRegaly:
            tmpMap[regal[0]][regal[1]] = 2
        return tmpMap
