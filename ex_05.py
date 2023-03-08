#5

pression = float(input("Entrez la pression : "))
volume = float(input("Entrez le volume : "))

pSeuil = 2.3
vSeuil = 7.41

if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat !")
elif pression > pSeuil:
    print("La pression est supérieure au seuil. Augmentez le volume de l'enceinte.")
elif volume > vSeuil:
    print("Le volume est supérieur au seuil. Diminuez le volume de l'enceinte.")
else:
    print("Tout va bien.")