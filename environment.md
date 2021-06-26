# Raport działania środowiska
-----

### Założenia projektu

Projekt ma przedstawiać działanie niektórych aspektów sztucznej inteligencji na podstawie inteligentnego magazynu. Naszym agentem jest wózek widłowy poruszający się po kracie.

### Podprojekty

* Rozpoznawanie cech paczki na podstawie zdjęcia (uczenie sieci neuronowych). W dowolnym momencie działania programu będzie można dodać zdjęcie paczki, która zostanie przeanalizowana pod kątem jego cech. Następnie zostanie przekazane do rozłożenia na magazynie za pomocą kolejnego podprojektu, lub ręcznie, w zależności od wyboru użytkownika. Wykorzystane zostaną do tego biblioteki YOLOv3 oraz OpenCV.
* Wykorzystanie uczenia drzew decyzyjnych do decydowania na które regały rozmieścić paczkę, na podstawie jej cech. Zbiór uczący byłby wyznaczany za pomocą algorytmu na początku działania każdego programu, ponieważ musiałby się on dostosować do konktretnych warunków podanych przez użytkownika. Następnie po wciśnięciu konkretnego przycisku, drzewo decyzyjne decydowałoby w którą konkretną lokalizację umieścić przesyłkę. Wykorzystana zostanie biblioteka sklearn.
* Wykorzystanie algorytmów genetycznych do znalezienia najoptymalniejszej drogi pomiędzy zajętymi regałami a miejscami oddania paczek w celu oddania paczki przy najmniejszym koszcie.

### Wykonanie

Do wykonania projektu w głównej mierze wykorzystany został język Python 3, wraz z bibliotekami:
* easygui - biblioteka użyta głównie przy starcie programu w celu pobrania od użytkownika wielkości kraty oraz ilości konkretnych regałów, ale również później do wyświetlania krótkich komunikatów.
* pygame - biblioteka użyta to wizualnej reprezentacji kraty wraz z agentem.
* YOLOv3 - Biblioteka użyta do rozpoznawania cech paczki.
* OpenCV - Biblioteka użyta do rozpoznawania cech paczki.
* sklearn - Biblioteka do obsługi drzew decyzyjnych.

### Klasy programu

Klasy projektu:

* Generate (z pliku generate.py) - Klasa służąca do generowania mapy.
* MainWindow (z pliku program.py) - Klasa służąca do wyświetlenia okna. Klasa ta zawiera również główną pętlę programu.
* Box (z pliku box.py) - klasa reprezentująca paczkę.

Klasy przedstawiające obiekty na kracie:

* BoxOnTheFloor (z pliku boxOnTheFloor.py) - Klasa przedstawiająca paczkę leżącą na kracie.
* Floor (z pliku floor.py) - Klasa przedstawiająca podłogę na kracie.
* Shelf (z pliku shelf.py) - Klasa przedstawiająca regał na kracie.
* UnboxOnTheFloor (z pliku unboxOnTheFloor.py) - Klasa przedstawiająca miejscę do odkładania paczek na kracie.
* Wall (z pliku wall.py) - Klasa przedstawiająca ścianę na kracie.
* Wheel (z pliku wheel.py) - Klasa przedstawiająca wózek widłowy na kracie.

### Działanie środowiska

Aktualnie gotowe jest środowisko w którym agent może się poruszać. Nie ma gotowych implementacji z zakresu sztucznej inteligencji. Można również rozmieszczać paczki oraz usuwać je z magazynu. Po kliknięciu w polu gry pojawia się paczka na podłodze. Można ją rozmieścić w magazynie kierując się do konkretnego regału i próbując w niego wejść. Na takiej samej zasadzie działa usuwanie paczek, a po odwiezieniu paczki w przeciwległą odnogę od tej w której się pojawiła paczka automatycznie zniknie z wózka.

#### Start programu

Po uruchomieniu programu musimy podać jakiej wielkości kratę chcemy uzyskać, a następnie jakie ilości których regałów chcemy posiadać na magazynie.

![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/1.png)

#### Okno programu

Gdy ukaże nam się okno programu możemy poruszać się wózkiem po magazynie. Używamy do tego strzałek.

![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/2.png)

#### Pojawienie się paczki

Gdy klikniemy na pole gry na planszy pojawi się paczka (w finalnej wersji, od użytkownika zostanie pobrana grafika przedstawiająca paczkę, która zostanie automatycznie sprawdzona i rozmieszczona na magazynie).

![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/3.png)

#### Rozmieszczenie na magazynie

Po wjechaniu wózkiem w paczkę, zostanie automatycznie pobrana na wózek. Gdy wjedziemy w regał (koniecznie od dobrej strony) paczka zostanie automatycznie rozmieszczona na tym regale.

![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/4.png)

#### Usunięcie paczki z magazynu

Gdy wjedziemy pustym wózkiem w regał na którym znajduje się paczka, paczka zostanie automatycznie pobrana na wózek. Jeśli natomiast wjedziemy w przeciwną odnogę magazynu, niż tą z której pobraliśmy na początku paczkę, zostanie usunięta z wózka i magazynu.

![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/5.png)

#### Demonstracja działania dla trzech paczek

[Link do filmu demo](https://git.wmi.amu.edu.pl/s444399/AI/src/master/demo/video.mp4)