#megoldas
def eredmeny(jatekospont, geppont):
    #teszt
    jatekoslista = []
    geplista = []
    jatekoslista.append(jatekospont)
    geplista.append(geppont)

    if jatekospont > 21:
        print("A játékos vesztett!")
    elif geppont > 21:
        print("A gép vesztett nyertél!")