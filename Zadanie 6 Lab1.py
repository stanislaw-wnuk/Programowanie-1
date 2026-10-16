temperatura = input("Podaj obecną temperaturę: ")
osoba = input("Czy ktoś jest w domu? ")
okno = input("Czy okno jest otwarte? ")
if okno == "tak":
    print("Ogrzewanie: WYŁĄCZONE")
    print("Przyczyna: otwarte okno")
elif okno == "nie" and osoba == "tak":
    print("Ogrzewanie: WŁĄCZONE na temperaturę poniżej 20 stopni")
elif okno == "nie" and osoba == "nie":
    print("Ogrzewanie: WŁĄCZONE na temperaturę poniżej 16 stopni")
else:
    print("Ogrzewanie: WYŁĄCZONE")
        