liste = [17, 38, 10, 25, 72]

liste.sort()
print(liste, "sort")

liste.append(12)
print(liste, "append")

liste.reverse()
print(liste, "reverse")

print(liste.index(17), "index")

liste.remove(38)
print(liste, "remove")

print(liste[1:3], "display 2nd and 3rd elements")

print(liste[:2], "display 1st and 2nd elements")

print(liste[2:], "display 3 to last elements")

print(liste[:])