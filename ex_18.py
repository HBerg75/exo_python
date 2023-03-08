chaine = input("Veuillez saisir une chaîne de caractères : ")
if "@" in chaine and chaine.endswith(".com"):
    indexPoint = chaine.index(".")
    print("C'est un email valide.")
    if len(chaine[indexPoint+1:]) <= 3:
        print("Le domaine est valide.")
    else:
        print("Le domaine n'est pas valide.")
else:
    print("Ce n'est pas un email valide.")