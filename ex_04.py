#4
mot1 = input("Entrez un premier mot: ")
mot2 = input("Entrez un deuxième mot: ")

if mot1 < mot2:
    print(mot1, "est avant", mot2)
elif mot1 > mot2:
    print(mot2, "est avant", mot1)
else:
    print(mot1, "et", mot2, "sont égaux")
