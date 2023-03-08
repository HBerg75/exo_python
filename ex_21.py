def save_file():
    x = int(input("Entrez un nombre: "))

    with open("data.txt", "w") as f:
        for i in range(x):
            s = input(f"entrez la chaine de caractère {i+1}: ")
            f.write(s + "\n")

    print(f"les {x} chaines de caractères ont été enregistrées dans le fichier data.txt")

save_file()