import pandas as pd
import matplotlib.pyplot as plt

studenci = []

while True:
    ilość = int(input("\nPodaj liczbę studentów: "))
    if ilość < 1:
        print("Liczba studentów musi być większa od 1")
    else:
        for i in range(ilość):
            imię = input("\nPodaj imię studenta " + str(i + 1) + ": ")
            nazwisko = input("Podaj nazwisko studenta " + str(i + 1) + ": ")
            punkty = float(input("Podaj punkty studenta " + str(i + 1) + ": "))
            student = {'Imię': imię, 'Nazwisko': nazwisko, 'Punkty': punkty}
            studenci.append(student) 
            def przypisz_ocene(punkty):
                if punkty < 50: return 2.0
                elif punkty < 60: return 3.0
                elif punkty < 70: return 3.5
                elif punkty < 80: return 4.0
                elif punkty < 90: return 4.5
                else: return 5.0
        df = pd.DataFrame(studenci)
        df['Ocena'] = df['Punkty'].apply(przypisz_ocene)

        print(df)   
        print("Średnia conajmniej 3: " + str(df[df['Ocena'] >= 3]['Ocena'].mean()))
        
        print(df.sort_values("Punkty", ascending=False))
        
        plt.bar(df["Nazwisko"], df["Ocena"])
        plt.title("Wyniki egzaminu")
        plt.xlabel("Student")
        plt.ylabel("Ocena")
        plt.ylim(0, 5.5)
        plt.tight_layout()
        plt.show()
        

