## Raport z wykonania części indywidualnej projektu
## Kijowski Michał

### Omówienie projektu

Projekt polega na dodaniu automatycznej identyfikacji paczek przychodzących do magazynu, na podstawie ich zdjęcia. Do wykonania projektu wykorzystałem uczenie sieci neuronowych (yolov3). Po otrzymaniu pliku graficznego przedstawiającego paczkę, program szuka na niej piktogramów aby zidentyfikować tę paczkę.

Wyróżniamy:

| Identyfikacja | Wyszukiwane piktogramy |
| -------- | -------- |
| Kruche | ![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/kruche.png) |
| Niebezpieczne | ![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/electrical.png) ![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/biohazard.png) |
| Radioaktywne | ![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/radioactive.png) |
| Łatwopalne | ![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/flammable.png) |

Jeśli nie znajdziemy żadnego z piktogramów, paczka jest klasyfikowana jako zwykła.

### Uczenie modelu

Program ten dysponuje pięcioma klasami, są to:
* kruche
* radioaktywne
* zagrożenia elektryczne
* biohazard
* latwopalne

Dla każdej klasy został przygotowany zbiór przedstawiający piktogramy reprezentowane przez te klasy:
* kruche - 137 zdjęć
* radioaktywne - 136 zdjęć
* zagrożenia elektryczne - 141 zdjęć
* biohazard - 144 zdjęć
* latwopalne - 120 zdjęć

Dla każdego pliku przygotowałem plik tekstowy o takiej samej nazwie (różniącej się tylko rozszerzeniem), w którym zawarte są współrzędne obiektów które chcemy wyszukiwać. I tak w każdej lini dla każdego obiektu na danym zdjęciu, zgodnie ze schematem:

<object-class> <x> <y> <width> <height>

Z tak przygotowanego zbioru wybrałem losowo niewielką część jako zbiór testowy.

Nasz zbiór uczący używamy w programie [darknet](https://github.com/pjreddie/darknet) do wygenerowania wag dla sieci. Wykorzystałem do tego pretrenowany model i dostosowałem go do potrzeb tego projektu z wykorzystaniem właśnie tego zbioru.

Współczynnik recall (część wspólna obiektu i detekcji przez rozmiar obiektu) dla poszczególnych etapów uczenia na podstawie zbioru testowego:

| Liczba iteracji | Współczynnik recall |
| -------- | -------- |
| 100 | 34.62 % |
| 200 | 35.14 % |
| 500 | 39.47 % |
| 1000 | 53.49 % |
| 5000 | 75.56 % |
| 15000 | 73.33 % |
| 30000 | 77.42 % |
| 40000 | 84.78 % |

### Integracja projektu

Integracja wykonana jest w pliku program.py

Mój podprojekt wywoływany jest po wciśnięciu lewego przycisku myszy. 

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
Sprawdzamy oczywiście czy lobby na paczki jest puste a jeśli tak to wywołujemy metodę fileopenbox z klasy easygui pozwalającą na wybranie pliku w ładny graficzny sposób.

![](https://git.wmi.amu.edu.pl/s444399/AI/raw/master/demo/a.png)

Następnie sprawdzamy czy jest to plik graficzny jeśli nie, powtarzamy to do skutku, lub zamknięcia okna.

Jeśli mamy już plik graficzny to ścieżka do niego jest przekazywana do klasy podprojektu której obiektem jest neurons a metodą którą wykonujemy jest whatIsIt.

### Implementacja projektu

Implementacja projektu znajduje się w klasie Neurons z pliku neurons.py.

class Neurons:
    def __init__(self):
        pass
    def get_output_layers(self, net):
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers
    def whatIsIt(self, path):
        image = cv2.imread(path)
        scale = 0.00392
        classes = None
        with open("yolov3.txt", 'r') as f:
            classes = [line.strip() for line in f.readlines()]
        net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        blob = cv2.dnn.blobFromImage(image, scale, (608, 608), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(self.get_output_layers(net))
        class_ids = []

W pierwszej części pliku wczytujemy wszystko zgodnie z zasadami detekcji dla tej metody. Wczytujemy naszą grafikę (ścieżka ze zmiennej path), model (yolov3.weights), nazwy klas (yolov3.txt), oraz konfigurację (yolov3.cfg). Następnie tworzymy sieć z modułu dnn (Deep Neural Networks) pakietu opencv (cv2) oraz tworzymy pustą listę na nasze przyszłe detekcje. Do listy outs pobieramy detekcje.

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.2:
                    class_ids.append(class_id)
        y = [classes[ids] for ids in  class_ids]

Gdy już mamy detekcje w liście outs, sprawdzamy które z nich mają prawdopodobieństwo większe niż 20% i dodajemy je do listy class_ids. Następnie zapisujemy nazwy tych klas do listy y za pomocą listy składanej.

        x = [0, 0, 0, 0, 0]
        if "kruche" in y:
            x[1]=1
        elif "niebezpieczne" in y:
            x[4]=1
        elif "biohazard" in y:
            x[4]=1
        elif "radioaktywne" in y:
            x[3]=1
        elif "latwopalne" in y:
            x[2]=1
        return [list(x)]

następnie sprawdzamy detekcję i generujemy listę z jedynką na pozycji odpowiadającej odpowiedniej detekcji, którą następnie zwracamy.