#megoldas
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    #teszt
    jatekospont: int = 0
    geppont: int = 0
    if jatekospont > 21:
        print("A játékos vesztett!")
    elif geppont > 21:
        print("A gép vesztett nyertél!")

def szamolas(lapok)->int:
    pontok: int = 0
    i: int = 0
    while i < len(lapok):
        pontok += lapok[i]
        i += 1
    return pontok