chaine = input("Veuillez saisir une chaîne de caractères : ")
reverse = chaine[::-1]

if chaine == reverse:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")