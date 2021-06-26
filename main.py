from easygui import *
from program import MainWindow
import os;

def main():

    good = False

    while (True):

        good = True
        fieldValues = multenterbox("Wprowadź warunki początkowe", "Start programu", ["Szerekość kraty (>=6)", "Wysokość kraty (>=7)", "Ilość regałów kruchych", "Ilość regałów łatwopalnych", "Ilość regałów radioaktywnych", "Ilość regałów niebezpiecznych"])
        if(fieldValues[0].isnumeric() and (fieldValues[0]!="")):
            if(int(fieldValues[0])<=5):
                msgbox("Szerokość kraty jest zbyt mała, aby można było uruchomić program", "Błąd")
                good = False
        elif(good==True):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False
        if(fieldValues[1].isnumeric() and (fieldValues[0]!="")):
            if((int(fieldValues[1])<=6) and (good==True)):
                msgbox("Wysokość kraty jest zbyt mała, aby można było uruchomić program", "Błąd")
                good = False
        elif (good == True):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False
        if ((fieldValues[2].isnumeric()) and (fieldValues[3].isnumeric()) and (fieldValues[4].isnumeric()) and (fieldValues[5].isnumeric()) and (fieldValues[2]!="") and (fieldValues[3]!="") and (fieldValues[4]!="") and (fieldValues[5]!="") and (good==True)):
            sum = int(fieldValues[2])+int(fieldValues[3])+int(fieldValues[4])+int(fieldValues[5])
            allow = 6+(((int(fieldValues[0])-6)//3)*2)
            if(sum>allow):
                msgbox("Magazyn zbyt mały co by pomieścił tyle regałów", "Błąd")
                good = False
        elif (good == True):
            msgbox("Wartość nie jest liczbą", "Błąd")
            good = False
        if good:
            window = MainWindow(int(fieldValues[0]), int(fieldValues[1]), int(fieldValues[2]), int(fieldValues[3]), int(fieldValues[4]), int(fieldValues[5]));
            break
        """
        szerokosc = 15#min 6
        wysokosc = 10     #min 7
        kruche = 1
        latwopalne = 1
        radioaktywne = 1
        niebezpieczne= 1
        window = MainWindow(szerokosc, wysokosc, kruche, latwopalne, radioaktywne, niebezpieczne);
        """

main()