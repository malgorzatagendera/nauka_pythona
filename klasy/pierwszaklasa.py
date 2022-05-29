#Najprostszy sposob definiowania obiektu
#Pass to miejsce dla funkcjonalnosci ktora bedzie dodana pozniej
#Pass moze byc uzyte w ciele metody (a body) ktore nic nie robi

class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzylismy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")

    #tworzymy obiekt na podst klasy, podajemy nazwe obiektu (paletka_a) i
    #wywlojemy konstruktor klasy (Paletka())
def testklasy() :
    paletka_a = Paletka("czerwony")
    paletka_b = Paletka("niebieski")
    print("*********************************")
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i metody:")
    print(dir(paletka_a))
    print("*********************************")
    print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne wlasciwosci i metody:")
    print(dir(paletka_b))
    print("*********************************")
    print(f"Kolor dla paletka_a): {paletka_a.kolor_obiektu}")
    print(f"Kolor dla paletka_b): {paletka_b.kolor_obiektu}")
