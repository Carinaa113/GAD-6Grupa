# cuvant = ' o n o m a t o p e e'
"""
daca litera de inceput si litera de sfarsit se gasesc in interiorul cuvantului, litera trebuie sa fie vizibila
cuvant = 'o _ o _ _ _ o _ e e'
7 incercari
"""
cuvant_de_ghicit = 'onomatopee'.lower()
cuvant = list(cuvant_de_ghicit)
for index, valoare in enumerate(cuvant):
    if cuvant[0] != valoare and cuvant[-1] != valoare:
        cuvant[index] = '_'
cuvant_de_afisat = ' '.join(cuvant)
print(f"Cuvantul de ghicit este: {cuvant_de_afisat}")
""" sa nu fie cifra => string.isdigit()
    sa nu introduca mai mult de 1 caracter => len(string) > 1
    sa nu fie spatiu
"""
litere_incercate = set()
numar_incercari = 0
while numar_incercari < 7:
    if len(list(litere_incercate)) > 0:
        print(f'Literele incercate sunt: {",".join(litere_incercate)}')
    litera_de_incercat = input("Adauga o litera: ").lower()
    while litera_de_incercat.isalpha() is False or len(litera_de_incercat) > 1 or litera_de_incercat in ["", " "]:
        if litera_de_incercat.isalpha() is False:
            print("Te rugam sa adaugi o litera. ")
        if len(litera_de_incercat) > 1:
            print("Ai adaugat mai multe caractere. Ai voie sa adaugi un singur caracter.")
        if litera_de_incercat in ["", " "]:
            print("Ai adaugat un spatiu. Te rugam sa introduci un caracter")
        litera_de_incercat = input("Adauga o litera: ").lower()
    if litera_de_incercat not in cuvant_de_ghicit:
        numar_incercari += 1
        litere_incercate.add(litera_de_incercat)
    elif litera_de_incercat in cuvant_de_ghicit and (cuvant_de_ghicit[0] != litera_de_incercat and
                                                     cuvant_de_ghicit[-1] != litera_de_incercat):
        for index, valoare in enumerate(cuvant_de_ghicit):
            if valoare == litera_de_incercat:
                cuvant[index] = litera_de_incercat
    if numar_incercari == 7:
        print(f"Ai pierdut. Cuvantul initial era: {cuvant_de_ghicit}")
    elif '_' not in cuvant:
        print("Ai castigat")
        break
    else:
        print(f"Mai ai {7 - numar_incercari} incercari")
    # if (numar_incercari_ramase := 7 - numar_incercari) and numar_incercari_ramase > 0:
    #     print(f"Mai ai {numar_incercari_ramase} incercari")
        print(" ".join(cuvant))