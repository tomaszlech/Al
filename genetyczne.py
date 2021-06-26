from funkcje import *
from Gene import Gene

def start(data, wheel, dane):

    ileGeneracji = int(dane[4])
    ileWPopulacji = int(dane[0])
    fragment = float(dane[1])
    mutacja = float(dane[2])
    unbox = int(dane[3])
    """
    ileGeneracji = 200
    ileWPopulacji = 16
    fragment = 0.5
    mutacja = 0.05
    unbox = 3
    """
    data.kordyWozka = (wheel.ns, wheel.we)
    data.jakLiczycKoszt = unbox

    randomPopulation = genRandomPopulation(data, ileWPopulacji)
    for i in range(ileGeneracji):
        if i == 0:
            populacjaFitness = fitnessDlaPopulacji(randomPopulation, data)
        else:
            #chrom2 = podajDwaChromosomy(populacjaFitness[0], populacjaFitness[1])
            x = genPopulacje(data,populacjaFitness[0], populacjaFitness[1], ileWPopulacji, fragment, mutacja)
            populacjaFitness = fitnessDlaPopulacji(x, data)
            #del x

            data.histZmian.append(data.best[1])


    #rysujWykres(data)




def generateGeny(data):
    geny = []
    zajeteRegaly = data.zajeteRegaly[:]
    for r in zajeteRegaly:
        g = Gene()
        g.kordy = r
        g.unbox1 = policzCost(data.astarMap,r,data.unbox[0])
        if(len(data.unbox) > 1):
            g.unbox2 = policzCost(data.astarMap,r,data.unbox[1])
        geny.append(g)
    return geny



def genRandomChromosome(data):
    chromosome = generateGeny(data)
    random.shuffle(chromosome)
    unboxLastGen = None

    for gen in chromosome:
        gen.unboxWczesniejszegoGenu = unboxLastGen
        krotkaKosztJakiUnbox = wybierzUnbox(gen, data.jakLiczycKoszt)
        unboxLastGen = krotkaKosztJakiUnbox[1]
        gen.kordyUnboxa = data.unbox[krotkaKosztJakiUnbox[1]]
    return chromosome

def genRandomPopulation(data, ileWPopulacji):
    populacja = []
    for i in range(ileWPopulacji):
        populacja.append(genRandomChromosome(data))
    return populacja

def podajDwaChromosomy(populacja, chromFitness):

    bestValue = min(chromFitness)
    bestChromIndex = chromFitness.index(bestValue)
    chrom1 = populacja[bestChromIndex]
    populacja.pop(bestChromIndex)
    chromFitness.pop(bestChromIndex)

    bestValue = min(chromFitness)
    bestChromIndex = chromFitness.index(bestValue)
    chrom2 = populacja[bestChromIndex]
    populacja.pop(bestChromIndex)
    chromFitness.pop(bestChromIndex)

    return (chrom1, chrom2)

def fitness(chromosome, data):
    koszt = 0
    unboxPoprzedniegoGenu = None

    for item, gen in enumerate(chromosome):
        if(item == 0):
            koszt += policzCost(data.astarMap, data.kordyWozka, gen.kordy)
            krotkaKosztJakiUnbox = wybierzUnbox(gen, data.jakLiczycKoszt)
            koszt += krotkaKosztJakiUnbox[0]
            unboxPoprzedniegoGenu = krotkaKosztJakiUnbox[1]

        else:
            if unboxPoprzedniegoGenu == 0:
                koszt += gen.unbox1
            elif unboxPoprzedniegoGenu == 1:
                koszt += gen.unbox2

            krotkaKosztJakiUnbox = wybierzUnbox(gen, data.jakLiczycKoszt)
            koszt += krotkaKosztJakiUnbox[0]
            unboxPoprzedniegoGenu = krotkaKosztJakiUnbox[1]


    return koszt


def fitnessDlaPopulacji(populacja, data):
    tmpPopulacja = populacja[:]
    chromFitness = []

    for chrom in populacja:
        chromFitness.append(fitness(chrom,data))

    bestValue = min(chromFitness)
    bestChromIndex = chromFitness.index(bestValue)
    pierwsza = tmpPopulacja[bestChromIndex]
    if (data.best == None):
        data.best = (pierwsza[:],bestValue)
    elif(data.best[1] > bestValue):
        data.best = (pierwsza[:],bestValue)
    data.doWykresu.append(bestValue)
    """
    tmpPopulacja.pop(bestChromIndex)
    chromFitness.pop(bestChromIndex)

    bestValue = min(chromFitness)
    bestChromIndex = chromFitness.index(bestValue)
    druga = tmpPopulacja[bestChromIndex]
    tmpPopulacja.pop(bestChromIndex)
    chromFitness.pop(bestChromIndex)
    """

    return (tmpPopulacja, chromFitness)

def crossover(data,pierwszy, drugi, fragmentLiczba, wspMutacji):
    ileWChrom = len(pierwszy)
    tmp = random.randint(0, ileWChrom-fragmentLiczba)
    kordyFragment = (tmp,tmp+fragmentLiczba)
    nowyChrom = [Gene() for q in range(ileWChrom)]
    iterator = kordyFragment[1]
    pomIterator = kordyFragment[1]
    usedKordy = []
    for i in range(kordyFragment[0],kordyFragment[1]):
        nowyChrom[i].kordy = pierwszy[i].kordy
        nowyChrom[i].unbox1 = pierwszy[i].unbox1
        nowyChrom[i].unbox2 = pierwszy[i].unbox2
        usedKordy.append(pierwszy[i].kordy)

    for x in range(ileWChrom):
        if(iterator > ileWChrom - 1):
            iterator = 0
        if(pomIterator > ileWChrom - 1):
            pomIterator = 0
        if(nowyChrom[iterator].kordy == None and drugi[pomIterator].kordy not in usedKordy):
            nowyChrom[iterator].kordy = drugi[pomIterator].kordy
            nowyChrom[iterator].kordy = drugi[pomIterator].kordy
            nowyChrom[iterator].unbox1 = drugi[pomIterator].unbox1
            nowyChrom[iterator].unbox2 = drugi[pomIterator].unbox2
            iterator += 1
            pomIterator += 1
        else:
            pomIterator +=1

    nowyChrom = mutate(wspMutacji, nowyChrom)
    unboxLastGen = None



    for gen in nowyChrom:
        gen.unboxWczesniejszegoGenu = unboxLastGen
        krotkaKosztJakiUnbox = wybierzUnbox(gen, data.jakLiczycKoszt)
        unboxLastGen = krotkaKosztJakiUnbox[1]
        gen.kordyUnboxa = data.unbox[krotkaKosztJakiUnbox[1]]

    return nowyChrom


def genPopulacje(data,populacja, chromFitness, ileWPopulacji, fragmentLiczba, wspMutacji):
    ileWChrom = len(populacja[0])
    fragment = round(fragmentLiczba*ileWChrom)
    if(fragment == 1):
        fragment +=1
    nowaPopulacja = []

    for i,index in enumerate(range(ileWPopulacji)):
        if index % 2 == 0:
            dwaChrom = podajDwaChromosomy(populacja,chromFitness)
        nowaPopulacja.append(crossover(data,dwaChrom[0],dwaChrom[1],fragment, wspMutacji))

    return nowaPopulacja

def mutate(wspMutacji, chrom): #w zaleznosci od tego jak wiele mutwac wybierz pary i zamien miejscami
    ileWChrom = len(chrom)
    ileZmian = round(ileWChrom * wspMutacji)
    for i in range(ileZmian):
        pom = None
        pierw = random.randint(0,ileWChrom - 1)
        drug = random.randint(0,ileWChrom - 1)
        pom = chrom[pierw]
        chrom[pierw] = chrom[drug]
        chrom[drug] = pom
    return chrom