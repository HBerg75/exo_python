for i in range(4):
    print(i, " les entiers de 0 à 3")

for i in range(4, 8):
    print(i, "les entiers de 4 à 7")

for i in range(2, 9, 2):
    print(i, " les entiers de 2 à 8 par pas de 2")



chose = [0, 1, 2, 3, 4, 5]

# Test de l'appartenance de 3 et 6 à la liste chose
print(3 in chose)  # True
print(6 in chose)  # False