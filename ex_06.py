chaine = input("Veuillez saisir une chaîne de caractères : ")

if "@" in chaine and chaine.endswith(".com"):
    print("C'est un email valide.")
else:
    print("Ce n'est pas un email valide.")
