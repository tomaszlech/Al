class Generate:
    @staticmethod
    def generate(szerokosc, wysokosc, kruche, latwopalne, radioaktywne, niebezpieczne):
        # 1 - sciana
        # 2 - podłoga
        # 3 - regał od dołu (zwykly)
        # 4 - regał od gory (zwykly)
        # 5 - regał od lewej (zwykly)
        # 6 - regał od prawej (zwykly)
        # 7 - regał od dołu (kruche)
        # 8 - regał od gory (kruche)
        # 9 - regał od lewej (kruche)
        # 10 - regał od prawej (kruche)
        # 11 - regał od dołu (latwopalne)
        # 12 - regał od gory (latwopalne)
        # 13 - regał od lewej (latwopalne)
        # 14 - regał od prawej (latwopalne)
        # 15 - regał od dołu (radioaktywne)
        # 16 - regał od gory (radioaktywne)
        # 17 - regał od lewej (radioaktywne)
        # 18 - regał od prawej (radioaktywne)
        # 19 - regał od dołu (niebezpieczne)
        # 20 - regał od gory (niebezpieczne)
        # 21 - regał od lewej (niebezpieczne)
        # 22 - regał od prawej (niebezpieczne)
        # 23 - unboxOnTheFloor
        all = []
        tmp  = []
        for i in range(0, wysokosc):
            for j in range(0, szerokosc):
                tmp.append(2)
            all.append(tmp)
            tmp = []
        for i in range(0, szerokosc):
            all[0][i] = 1
            all[wysokosc-1][i] = 1
        for i in range(0, wysokosc):
            all[i][0] = 1
            all[i][szerokosc-1] = 1
        if (kruche>0):
            for i in range(2, szerokosc-2):
                all[1][i] = 7
            kruche-=1
        elif (latwopalne>0):
            for i in range(2, szerokosc-2):
                all[1][i] = 11
            latwopalne-=1
        elif (radioaktywne>0):
            for i in range(2, szerokosc-2):
                all[1][i] = 15
            radioaktywne-=1
        elif (niebezpieczne>0):
            for i in range(2, szerokosc-2):
                all[1][i] = 19
            niebezpieczne-=1
        else:
            for i in range(2, szerokosc-2):
                all[1][i] = 3
        if (kruche>0):
            for i in range(2, wysokosc-2):
                all[i][szerokosc-2] = 9
            kruche-=1
        elif (latwopalne>0):
            for i in range(2, wysokosc-2):
                all[i][szerokosc-2] = 13
            latwopalne-=1
        elif (radioaktywne>0):
            for i in range(2, wysokosc-2):
                all[i][szerokosc-2] = 17
            radioaktywne-=1
        elif (niebezpieczne>0):
            for i in range(2, wysokosc-2):
                all[i][szerokosc-2] = 21
            niebezpieczne-=1
        else:
            for i in range(2, wysokosc-2):
                all[i][szerokosc-2] = 5
        if (kruche>0):
            for i in range(2, szerokosc-2):
                all[wysokosc-2][i] = 8
            kruche-=1
        elif (latwopalne>0):
            for i in range(2, szerokosc-2):
                all[wysokosc-2][i] = 12
            latwopalne-=1
        elif (radioaktywne>0):
            for i in range(2, szerokosc-2):
                all[wysokosc-2][i] = 16
            radioaktywne-=1
        elif (niebezpieczne>0):
            for i in range(2, szerokosc-2):
                all[wysokosc-2][i] = 20
            niebezpieczne-=1
        else:
            for i in range(2, szerokosc-2):
                all[wysokosc-2][i] = 4
        if (kruche>0):
            for i in range(2, wysokosc-2):
                all[i][1] = 10
            kruche-=1
        elif (latwopalne>0):
            for i in range(2, wysokosc-2):
                all[i][1] = 14
            latwopalne-=1
        elif (radioaktywne>0):
            for i in range(2, wysokosc-2):
                all[i][1] = 18
            radioaktywne-=1
        elif (niebezpieczne>0):
            for i in range(2, wysokosc-2):
                all[i][1] = 22
            niebezpieczne-=1
        else:
            for i in range(2, wysokosc-2):
                all[i][1] = 6
        for j in range(3, szerokosc-4, 3):
            if (kruche > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j] = 9
                kruche -= 1
            elif (latwopalne > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j] = 13
                latwopalne -= 1
            elif (radioaktywne > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j] = 17
                radioaktywne -= 1
            elif (niebezpieczne > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j] = 21
                niebezpieczne -= 1
            else:
                for i in range(3, wysokosc - 3):
                    all[i][j] = 5
            if (kruche > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j+1] = 10
                kruche -= 1
            elif (latwopalne > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j+1] = 14
                latwopalne -= 1
            elif (radioaktywne > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j+1] = 18
                radioaktywne -= 1
            elif (niebezpieczne > 0):
                for i in range(3, wysokosc - 3):
                    all[i][j+1] = 22
                niebezpieczne -= 1
            else:
                for i in range(3, wysokosc - 3):
                    all[i][j+1] = 6
        counter = 0
        for i in range(3, szerokosc - 3):
            counter+=1
            if counter==3:
                counter=0
                continue
            else:
                all[3][i] = 1
                all[wysokosc-4][i] = 1
        all[1][1] = 1
        all[1][3] = 1
        all[1][szerokosc-2] = 1
        all[wysokosc-2][1] = 1
        all[wysokosc-2][szerokosc-2] = 1
        all[0][2] = 2
        all[1][2] = 2
#zmiana miejsca zrzutu paczki, unboxOnTheFloor
        all[wysokosc-2][szerokosc-3] = 2
        all[wysokosc-1][szerokosc-3] = 23
        all[wysokosc-2][szerokosc-4] = 1


        all[wysokosc-2][2] = 2
        all[wysokosc-1][2] = 23
        all[wysokosc-2][3] = 1

        return all

