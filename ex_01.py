# 1

temps = 6.892
distance = 19.7
vitesse = distance / temps

print("La vitesse est de :", round(vitesse, 1), "m/s")


#2

nom = input("Entrez votre nom: ")
age = input("Entrez votre âge: ")

age = int(age)

print("Nom: ", nom)
print("Âge: ", age)

#3

nombre = float(input("Entrez un nombre: "))

if nombre >= 0:
    racine = nombre ** 0.5
    print("La racine carrée de", nombre, "est", racine)
else:
    print("Erreur")

#4
mot1 = input("Entrez un premier mot: ")
mot2 = input("Entrez un deuxième mot: ")

if mot1 < mot2:
    print(mot1, "est avant", mot2)
elif mot1 > mot2:
    print(mot2, "est avant", mot1)
else:
    print(mot1, "et", mot2, "sont égaux")

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
    