#Najprostszy sposob definiowania obiektu
#Pass to miejsce dla funkcjonalnosci ktora bedzie dodana pozniej
#Pass moze byc uzyte w ciele metody (a body) ktore nic nie robi

class Paletka:
    pass

    #tworzymy obiekt na podst klasy, podajemy nazwe obiektu (paletka_a) i
    #wywlojemy konstruktor klasy (Paletka())
def testklasy() :
    paletka_a = Paletka()
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne wlasciwosci i metody:")
    print(dir(paletka_a))
