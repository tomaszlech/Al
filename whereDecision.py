import pandas as pd
import graphviz
import sklearn
from sklearn.tree import DecisionTreeClassifier
from ast import literal_eval as make_tuple

class WhereDecision:
    def __init__(self):
        pass

    def recognize(self, recognize, regals):
        zwykle = []
        kruche = []
        latwopalne = []
        radioaktywne = []
        niebezpieczne = []
        lokacja = []
        for regal in regals:
            if (regal[2] == 1):
                zwykle.append(0)
                kruche.append(1)
                latwopalne.append(0)
                radioaktywne.append(0)
                niebezpieczne.append(0)
                lokacja.append(str("("+str(regal[0])+", "+str(regal[1])+")"))
            elif (regal[2] == 2):
                zwykle.append(0)
                kruche.append(0)
                latwopalne.append(1)
                radioaktywne.append(0)
                niebezpieczne.append(0)
                lokacja.append(str("("+str(regal[0])+", "+str(regal[1])+")"))
            elif (regal[2] == 3):
                zwykle.append(0)
                kruche.append(0)
                latwopalne.append(0)
                radioaktywne.append(1)
                niebezpieczne.append(0)
                lokacja.append(str("("+str(regal[0])+", "+str(regal[1])+")"))
            elif (regal[2] == 4):
                zwykle.append(0)
                kruche.append(0)
                latwopalne.append(0)
                radioaktywne.append(0)
                niebezpieczne.append(1)
                lokacja.append(str("("+str(regal[0])+", "+str(regal[1])+")"))
            else:
                zwykle.append(1)
                kruche.append(0)
                latwopalne.append(0)
                radioaktywne.append(0)
                niebezpieczne.append(0)
                lokacja.append(str("("+str(regal[0])+", "+str(regal[1])+")"))
        if len(zwykle) == 0:
            return [1, 2]
        z = list(zip(zwykle, kruche, latwopalne, radioaktywne, niebezpieczne))
        prenumeratorzy = pd.DataFrame({"lokacja": lokacja})
        prenumeratorzy["lokacja"], lokacja_kody = pd.factorize(prenumeratorzy["lokacja"])
        y = prenumeratorzy["lokacja"]
        drzewko = DecisionTreeClassifier(criterion="entropy")
        drzewko.fit(X=z, y=y)
        tmp = list(make_tuple(lokacja_kody[drzewko.predict(recognize)][0]))
        return tmp