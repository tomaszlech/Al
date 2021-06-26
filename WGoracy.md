## Podprojekt indywidualny - Weronika Gorący

### Wykorzystane metody uczenia

Do realizacji podprojektu wykorzystano drzewa decyzyjne do decydowania, na które regały należy umieścić paczkę na podstawie jej cech. Do implementacji drzew decyzyjnych w Pythonie wykorzystane zostały biblioteki *sklearn* i *pandas*.

### Omówienie kodu

Kod podprojektu znajduje się w klasie **whereDecision** w pliku [whereDecision.py](https://git.wmi.amu.edu.pl/s444399/AI/src/master/whereDecision.py). Wywołanie metody **recognize** odbywa się w klasie **program** w pliku [program.py](https://git.wmi.amu.edu.pl/s444399/AI/src/master/program.py).

```
whatIsIt = self.neurons.whatIsIt(easygui.fileopenbox("Wybierz zdjęcie paczki", "Wybierz zdjęcie paczki", filetypes = [["*.jpg", "*.jpeg", "*.png", "Pliki graficzne"]]))
where = self.whereDecision.recognize(whatIsIt, self.regalsik())
```

Do zmiennej **whatIsIt** zostaje zapisany typ otrzymanej paczki w formie tablicy binarnej, który został rozpoznany dzięki innemu podprojektowi, następnie wywoływana jest metoda **recognize** z parametrami **whatIsIt** i **self.regalsik()**.

Do tablicy **regals** zapisywane są dane wszystkich regałów wygenerowanych na planszy.

```
self.regals.append((i, j, (self.map[i][j]-3)//4))
```

Metoda **regalsik()** sprawdza czy regał z tablicy **regals** jest pusty i jeżeli tak, to umieszcza go w tablicy wyjściowej, która ostatecznie jest tablicą krotek zawierajacych informacje o wszystkich pustych regałach na planszy. Każda krotka zawiera informacje o współrzędnej Y i X regału oraz typ paczki jaki może być na niej przechowywany.

```
    def regalsik(self):
        tmp = []
        for regal in self.regals:
            if self.map[regal[0]][regal[1]].isOccupied()==False:
                tmp.append(regal)
        return tmp
```

### Uczenie modelu

Metoda **recognize** rozpoczyna od utworzenia zbioru uczącego na podstawie tabeli zawierającej informacje o pustych półkach na planszy. Dla każdego regału sprawdzany jest typ paczki, który może być na niej przechowywany, a następnie jest on dodawany do odpowiedniej tablicy. Tablica **lokacja** zawiera położenia wszystkich regałów na planszy.

```
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
```

Jeżeli wszystkie półki są zajęte, wózek zatrzyma się w swojej wyjściowej pozycji.

```
        if len(zwykle) == 0:
            return [1, 2]
```

Do zmiennej **z** zapisujemy połączone tablice wszystkich typów regałów, zaś do zmiennej **y** zapisujemy tabelę prenumeratorzy typu DataFrame z biblioteki *pandas*, która zawiera dane lokalizacji konkretnych regałów.

```
        z = list(zip(zwykle, kruche, latwopalne, radioaktywne, niebezpieczne))
        prenumeratorzy = pd.DataFrame({"lokacja": lokacja})
        prenumeratorzy["lokacja"], lokacja_kody = pd.factorize(prenumeratorzy["lokacja"])
        y = prenumeratorzy["lokacja"]
```

Zmienne **z** i **y** są naszym zbiorem uczącym.

### Implementacja

Do zmiennej **drzewko** zapisujemy drzewo decyzyjne z biblioteki *sklearn* utworzone za pomocą obiektu klasy **DecisionTreeClassifier** z parametrem konstruktora **criterion** ustawionym na **"entropy"**. Na drzewie wywołujemy metodę **fit**, która tworzy model danych w oparciu o nasz zbiór uczący. Po utworzeniu modelu danych możemy przewidzieć przynależność nowych przykładów, co robimy wywołując na drzewie metodę **predict** z parametrem uzyskanym na samym początku, który zawiera informację o rodzaju otrzymanej paczki. W ostateczności zwracamy krotkę zawierającą lokalizację, na której zostanie umieszczona paczka.

```
        drzewko = DecisionTreeClassifier(criterion="entropy")
        drzewko.fit(X=z, y=y)
        return list(make_tuple(lokacja_kody[drzewko.predict(recognize)][0]))
```

Ostatecznie lokalizacja, którą zwróciła metoda **recognize** zapisywana jest do zmiennej **where** (klasa **program**) i na tej podstawie wózek z pomocą algorytmu AStar wybiera odpowiednią ścieżkę do umieszczenia paczki.