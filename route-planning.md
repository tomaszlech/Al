## Strategia planowania ruchu

### Wykorzystane klasy

AStar - Klasa zawierająca działanie algorytmu.
AStarState - Klasa zawierająca reprezentację wierzchołka.

### Wymagania

1.Celem zadania jest zastosowanie strategii przeszukiwania przestrzeni stanów do problemu planowania ruchu agenta na kracie.

```
Agent porusza się po klinknięciu na aplikację oraz wybraniu jakiegokolwiek pliku graficznego. Zostanie tutaj zaimplementowane rozpoznawanie paczek, ale w tym wstępnym etapie lokacja dla paczki zostaje wybrana losowo. Wtedy za pomocą tego algorytmu znajdowana jest ścieżka od agenta do docku a także od docku do lokacji wybranej przez drzewo decyzyjne.
```

2.Należy wykorzystać „Schemat procedury przeszukiwania grafu stanów z uwzględnieniem kosztu“.

```
Jest uwzględniany koszt przejścia. Przechodzenie między środkowymi regałami ma 10 krotnie większy koszt niż alteriami po zewnętrznej stronie. Na poniższej grafice zielone ścieżki mają koszt 1 a czerwone 10.
```
![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/6.png)

3.Należy zaimplementować strategię A*, czyli zdefiniować funkcję wyznaczającą priorytet następ-ników uwzględniającą zarówno koszt jak i odpowiednią heurystykę.

```
Zastosowana została heurystyka ((([aktualnapozycjaY]-[CelY]) ** 2) + (([aktualnapozycjaX]-[CelX]) ** 2)
```

4.Agent powinien dysponować co najmniej następującymi akcjami: ruch do przodu, obrót w lewo,obrót w prawo.5. Koszt wjazdu na pola poszczególnych typów powinien być zróżnicowany.

```
Nasz agent oferuje ruchy do przodu, do tyłu, w lewo, w prawo. Jest to spowodowane wykonaniem programu przed pojawieniem się szczegółowych wymagań, natomiast w wymaganiach pierwotnych nie było takiego wymogu, a taka zmiana wymagałaby bardzo dużego nakładu pracy ponieważ nawet model ręcznego poruszania się po kracie bazował na takich ruchach jak powyżej, tak jak sposób wkładania konkretnych paczek na regały. Koszt jest zróżnicowany (patrz punkt 2). 
```
### Demonstracja działania środowiska

[Film prezentujący działanie środowiska](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/video2.mp4)

```
Na przykładzie widać działanie zróżnicowanego kosztu (podczas pierwszej paczki) - Agent woli wyjść spomiędzy regałów aby przejść po paczkę po głównych alteriach (zewnętrzne drogi) nawet jeśli droga ta jest dłuższa.
```

### Pętla główna - pseudokod

```
Jeśli istnieją wierzchołki do odwiedzenia:
    zwiększamy licznik operacji (stop w razie nieznalezienia rozwiązania po przekroczeniu liczny iteracji)
    pobieramy pierwszy wierzchołek do odwiedzenia
    jeśli natomiast jest wierzchołek o mniejszym koszcie to zajmiemy się nim najpierw
    stop jeśli przekroczyliśmy maksymalną liczbę operacji
    przenosimy wierzchołek z listy wierzchołków do odwiedzenia do tych już odwiedzonych
    jeśli nasz aktualny wierzchołek jest końcowym kończymy algorytm
```

### Pętla główna - kod w python

```
        while len(toVisit)>0:
            iterations=iterations+1
            current = toVisit[0]
            currentIndeks = 0
            for indeks, item in enumerate(toVisit):
                if item.g<current.g:
                    current = item
                    currentIndeks = indeks
            if iterations>max:
                return self.returnPath(current, grid)
            visited.append(current)
            toVisit.pop(currentIndeks)
            if current==endNode:
                return self.returnPath(current, grid)
            #funkcjanastępnika
```

### Funkcja następnika - pseudokod

```
Dla listy możliwych ruchów generujemy wszystkie możliwe następniki:
    sprawdzamy czy taki następnik nie wychodzi poza kratę
    sprawdzamy czy nie wchodzi on przypadkiem na regał albo ścianę
    jeśli nie nastąpił żaden z powyższych warunków dodajemy każdy taki następnik do listy
Dla listy następników:
    jeśli w odwiedzonych już istnieje taki wierzchołek to go ignorujemy
    jeśli nie istnieje to obliczamy f, g i h oraz dodajemy taki wierzchołek do listy wierzchołków do odwiedzenia
```

### Funkcja następnika - kod w python

```
            for new in moves:
                positions = (current.position[0]+new[0], current.position[1]+new[1])
                if (positions[0] > (noRows - 1) or
                    positions[0] < 0 or
                    positions[1] > (noColumns - 1) or
                    positions[1] < 0):
                    continue
                if grid[positions[0]][positions[1]]!=0:
                    continue
                children.append(AStarState(current, positions))
            for child in children:
                if len([visitedChild for visitedChild in visited if visitedChild==child])>0:
                    continue
                if child.position[0]<=(len(grid)-4) and child.position[0]>=3 and child.position[1]>=4 and child.position[1]<=(len(grid[0])-1):
                    child.g = current.g + (10 * cost)
                else:
                    child.g = current.g + cost
                child.h = (((child.position[0]-endNode.position[0]) ** 2) + ((child.position[1]-endNode.position[1]) ** 2))
                child.f = child.g + child.h
                if len([i for i in toVisit if child==i and child.g>i.g])>0:
                    continue
                toVisit.append(child)
             children = []
```