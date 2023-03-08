entier = None

while entier is None:
    try:
        entier = int(input("Entrez un entier: "))
        if entier < 1 or entier > 10:
            print("Vous n'avez pas saisi un entier entre 1 et 10")
            entier = None
    except ValueError:
        print("Vous n'avez pas saisi un entier")
        entier = None

print("Vous avez saisi l'entier", entier)