#megoldas
def eredmeny(jatekoslapok: [int], geplapok: [int]):
    #teszt
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