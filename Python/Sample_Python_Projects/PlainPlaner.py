# -*- coding: utf-8 -*-

class Samolot:
    """Klasa reprezentująca samolot"""

    def __init__(self, model, producent, liczba_miejsc, max_predkosc, max_wysokosc, typ="cywilny"):
        """
        Inicjalizacja samolotu

        Args:
            model (str): Model samolotu
            producent (str): Producent samolotu
            liczba_miejsc (int): Liczba miejsc pasażerskich lub bomb
            max_predkosc (int): Maksymalna prędkość w km/h
            max_wysokosc (int): Maksymalna wysokość w metrach
            typ (str): Typ samolotu ("cywilny", "wojskowy", "sportowy")
        """
        self.model = model
        self.producent = producent
        self.liczba_miejsc = liczba_miejsc
        self.max_predkosc = max_predkosc
        self.max_wysokosc = max_wysokosc
        self.typ = typ
        self.w_locie = False
        self.aktualna_wysokosc = 0
        self.liczba_pasazerow = 0
        self.liczba_bomb = 0

    def start(self):
        """Wystartuj samolotem"""
        if not self.w_locie:
            self.w_locie = True
            print(f"{self.model} wystartował!")
        else:
            print(f"{self.model} jest już w locie.")

    def ladowanie(self):
        """Wyląduj samolotem"""
        if self.w_locie:
            self.w_locie = False
            self.aktualna_wysokosc = 0
            print(f"{self.model} wylądował!")
        else:
            print(f"{self.model} już jest na ziemi.")

    def zmien_wysokosc(self, nowa_wysokosc):
        """
        Zmień wysokość lotu

        Args:
            nowa_wysokosc (int): Nowa wysokość w metrach
        """
        if self.w_locie:
            if nowa_wysokosc <= self.max_wysokosc:
                self.aktualna_wysokosc = nowa_wysokosc
                print(f"{self.model} leci na wysokości {self.aktualna_wysokosc}m")
            else:
                print(f"Za wysoko! Maksymalna wysokość dla {self.model}: {self.max_wysokosc}m")
        else:
            print(f"{self.model} musi najpierw wystartować!")

    def wznies_na_maksymalna_wysokosc(self):
        """Wznieś się na maksymalną wysokość"""
        if self.w_locie:
            self.aktualna_wysokosc = self.max_wysokosc
            print(f"{self.model} wznosi się na maksymalną wysokość: {self.max_wysokosc}m")
        else:
            print(f"{self.model} musi najpierw wystartować!")

    def zaladuj_pasazerow(self, liczba):
        """
        Załaduj pasażerów na pokład

        Args:
            liczba (int): Liczba pasażerów do załadowania
        """
        if self.typ == "wojskowy":
            print("Samolot wojskowy nie przewozi pasażerów! Użyj zaladuj_bomby()")
            return

        if self.liczba_pasazerow + liczba <= self.liczba_miejsc:
            self.liczba_pasazerow += liczba
            print(f"Załadowano {liczba} pasażerów. Razem: {self.liczba_pasazerow}/{self.liczba_miejsc}")
        else:
            print(f"Za dużo pasażerów! Dostępne miejsca: {self.liczba_miejsc - self.liczba_pasazerow}")

    def zaladuj_bomby(self, liczba):
        """
        Załaduj bomby (tylko samoloty wojskowe)

        Args:
            liczba (int): Liczba bomb do załadowania
        """
        if self.typ != "wojskowy":
            print("Tylko samoloty wojskowe mogą ładować bomby!")
            return

        if self.liczba_bomb + liczba <= self.liczba_miejsc:
            self.liczba_bomb += liczba
            print(f"Załadowano {liczba} bomb. Razem: {self.liczba_bomb}/{self.liczba_miejsc}")
        else:
            print(f"Za dużo bomb! Dostępna pojemność: {self.liczba_miejsc - self.liczba_bomb}")

    def info(self):
        """Wyświetl informacje o samolocie"""
        status = "w locie" if self.w_locie else "na ziemi"
        print(f"\n--- Informacje o samolocie ---")
        print(f"Model: {self.model}")
        print(f"Producent: {self.producent}")
        print(f"Typ: {self.typ}")
        print(f"Pojemność: {self.liczba_miejsc}")
        print(f"Maksymalna prędkość: {self.max_predkosc} km/h")
        print(f"Maksymalna wysokość: {self.max_wysokosc}m")
        print(f"Status: {status}")
        print(f"Wysokość: {self.aktualna_wysokosc}m")
        if self.typ == "wojskowy":
            print(f"Bomby: {self.liczba_bomb}/{self.liczba_miejsc}")
        else:
            print(f"Pasażerowie: {self.liczba_pasazerow}/{self.liczba_miejsc}")
        print("-----------------------------\n")


def wybierz_samolot():
    """Menu wyboru samolotu"""
    print("\n" + "="*50)
    print("   SYMULATOR LOTU - WYBIERZ SAMOLOT")
    print("="*50)
    print("\n1. Cessna 172 Skyhawk - Lekki jednoplatowiec")
    print("   • Miejsca: 4 pasażerów")
    print("   • Prędkość max: 226 km/h")
    print("   • Wysokość max: 4,300m\n")

    print("2. F-35 Lightning II - Myśliwiec wojskowy")
    print("   • Pojemność: 8 bomb")
    print("   • Prędkość max: 1,930 km/h")
    print("   • Wysokość max: 15,000m\n")

    print("3. Boeing 737 - Samolot pasażerski")
    print("   • Miejsca: 189 pasażerów")
    print("   • Prędkość max: 850 km/h")
    print("   • Wysokość max: 12,500m\n")

    wybor = input("Wybierz samolot (1-3): ")

    if wybor == "1":
        return Samolot("Cessna 172 Skyhawk", "Cessna", 4, 226, 4300, "sportowy")
    elif wybor == "2":
        return Samolot("F-35 Lightning II", "Lockheed Martin", 8, 1930, 15000, "wojskowy")
    elif wybor == "3":
        return Samolot("Boeing 737", "Boeing", 189, 850, 12500, "cywilny")
    else:
        print("Nieprawidłowy wybór! Domyślnie wybieram Cessna 172.")
        return Samolot("Cessna 172 Skyhawk", "Cessna", 4, 226, 4300, "sportowy")


def menu_ladowania(samolot):
    """Menu ładowania pasażerów lub bomb"""
    print("\n" + "="*50)
    print("   ZAŁADUNEK")
    print("="*50)

    if samolot.typ == "wojskowy":
        print(f"\nDostępna pojemność: {samolot.liczba_miejsc} bomb")
        try:
            liczba = int(input("Ile bomb chcesz załadować? "))
            samolot.zaladuj_bomby(liczba)
        except ValueError:
            print("Nieprawidłowa wartość!")
    else:
        print(f"\nDostępne miejsca: {samolot.liczba_miejsc} pasażerów")
        try:
            liczba = int(input("Ilu pasażerów chcesz załadować? "))
            samolot.zaladuj_pasazerow(liczba)
        except ValueError:
            print("Nieprawidłowa wartość!")


def symulacja_lotu(samolot):
    """Główna symulacja lotu"""
    print("\n" + "="*50)
    print("   SYMULACJA LOTU")
    print("="*50)

    # Wyświetl informacje
    samolot.info()

    # Start
    input("\nNaciśnij ENTER aby wystartować...")
    samolot.start()

    # Wznoszenie na maksymalną wysokość
    input("\nNaciśnij ENTER aby wznieść się na maksymalną wysokość...")
    samolot.wznies_na_maksymalna_wysokosc()

    # Informacje w locie
    samolot.info()

    # Lądowanie
    input("\nNaciśnij ENTER aby wylądować...")
    samolot.ladowanie()

    # Informacje po lądowaniu
    samolot.info()

    print("\n" + "="*50)
    print("   KONIEC SYMULACJI")
    print("="*50)


# Główny program
if __name__ == "__main__":
    # Wybór samolotu
    samolot = wybierz_samolot()

    # Menu ładowania
    menu_ladowania(samolot)

    # Symulacja lotu
    symulacja_lotu(samolot)
