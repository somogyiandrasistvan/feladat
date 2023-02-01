#megoldas
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jatekospont: int = szamolas(jatekoslapok)
    geppont: int = szamolas(geplapok)
    if jatekospont > 21:
        return "játékos vesztett!"
    elif geppont > 21:
        return "gép vesztett!"

def szamolas(lapok)->int:
    pontok: int = 0
    i: int = 0
    while i < len(lapok):
        pontok += lapok[i]
        i += 1
    return pontok

def jatekos_vesztett_teszt():
    jatekospontok = [10, 5, 7]
    geppontok = [2, 7, 9]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "játékos vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")
def gep_vesztett_teszt():
    jatekospontok = [10, 5, 7]
    geppontok = [2, 7, 9]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "gép vesztett!"
    if kapott == vart:
        print("A teszt sikeres!")
    else:
        print("A teszt megbukott")
def tesztek():
    jatekos_vesztett_teszt()

tesztek()