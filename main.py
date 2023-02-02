#megoldas
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    jatekospont: int = szamolas(jatekoslapok)
    geppont: int = szamolas(geplapok)
    jatekoslapok_osszeg = len(jatekoslapok)
    geplapok_osszeg = len(geplapok)
    if jatekospont <= 21 and geppont <= 21:
        if jatekospont > geppont:
            s = "Játékos nyert!"
        elif geppont > jatekospont:
            s = "Gép nyert!"
        elif geppont == jatekospont:
            if jatekoslapok_osszeg < geplapok_osszeg:
                s = "Játékos nyert!"
            elif jatekoslapok_osszeg > geplapok_osszeg:
                s = "Gép nyert!"
            else:
                s = "Döntetlen osztoztok a nyereségen"
    else:
        if jatekospont > 21:
            s = "Játékos vesztett!"
        if geppont > 21:
            s = "Gép vesztett!"
        if jatekospont > 21 and geppont > 21:
            s = "Döntetlen osztoztok a nyereségen"

    return s

def szamolas(lapok)->int:
    pontok: int = 0
    i: int = 0
    while i < len(lapok):
        pontok += lapok[i]
        i += 1
    return pontok
#tesztek
def jatekos_vesztett_teszt():
    jatekospontok = [10, 5, 7]
    geppontok = [2, 7, 9]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos vesztett!"
    if kapott == vart:
        print("Az első teszt sikeres!")
    else:
        print("Az első teszt megbukott")

def gep_vesztett_teszt():
    jatekospontok = [2, 7, 9]
    geppontok = [10, 5, 7]
    #teszt
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép vesztett!"
    if kapott == vart:
        print("A második teszt sikeres!")
    else:
        print("A második teszt megbukott")

def lapok_osszege_teszt():
    jatekospontok = [11, 11]
    geppontok = [10, 10]
    #teszt
    osszeg = szamolas(jatekospontok)
    if osszeg > 21:
        print("A harmadik teszt sikeres!")
    else:
        print("A harmadik teszt megbukott!")

def jatekos_kozelebb_teszt():
    jatekospontok = [9, 10]
    geppontok = [8, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A negyedik teszt sikeres!")
    else:
        print("A negyedik teszt megbukott")

def gep_kozelebb_teszt():
    jatekospontok = [8, 10]
    geppontok = [9, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("Az ötödik teszt sikeres!")
    else:
        print("Az ötödik teszt megbukott")

def gep_vesztett_dontetlen_teszt():
    jatekospontok = [9, 10]
    geppontok = [9, 5, 5]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Játékos nyert!"
    if kapott == vart:
        print("A hatodik teszt sikeres!")
    else:
        print("A hatodik teszt megbukott")

def jatekos_vesztett_dontetlen_teszt():
    jatekospontok = [9, 5, 5]
    geppontok = [9, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Gép nyert!"
    if kapott == vart:
        print("A hetedik teszt sikeres!")
    else:
        print("A hetedik teszt megbukott")

def dontetlen_teszt():
    jatekospontok = [10, 10]
    geppontok = [10, 10]
    kapott = eredmeny(jatekospontok, geppontok)
    vart = "Döntetlen osztoztok a nyereségen"
    if kapott == vart:
        print("A nyolcadik teszt sikeres!")
    else:
        print("A nyolcadik teszt megbukott")


def tesztek():
    jatekos_vesztett_teszt()
    gep_vesztett_teszt()
    lapok_osszege_teszt()
    jatekos_kozelebb_teszt()
    gep_kozelebb_teszt()
    gep_vesztett_dontetlen_teszt()
    jatekos_vesztett_dontetlen_teszt()
    dontetlen_teszt()


tesztek()