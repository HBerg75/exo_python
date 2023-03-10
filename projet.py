class AB:
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = [racine]
        self.gauche = gauche
        self.droite = droite
    
    def set_racine(self, valeur):
        self.racine = [valeur]
    
    def set_gauche(self, arbre):
        self.gauche = arbre
    
    def set_droite(self, arbre):
        self.droite = arbre
    
    def estVide(self):
        if self.racine == [None]:
            return True
        else:
            return False
    
    def afficher(self):
        print("Racine:", self.racine)
        print("Sous-arbre gauche:")
        if self.gauche:
            self.gauche.afficher()
        else:
            print("Vide")
        print("Sous-arbre droit:")
        if self.droite:
            self.droite.afficher()
        else:
            print("Vide")
            
    def taille(self):
        if self.estVide():   
            return 0
        else:
            size = 1
            if self.gauche:
                size += self.gauche.taille()
            if self.droite:
                size += self.droite.taille()
            return size
            
    def prefixe(self):
        if self.estVide():
            return 0
        else:
            result = [self.racine[0]]
            if self.gauche:
                result += self.gauche.prefixe()
            if self.droite:
                result += self.droite.prefixe()
            return result
        
    def infixe(self):
        if self.estVide():
            return 0
        else:
            result = []
            if self.gauche:
                result += self.gauche.infixe()
            result += [self.racine[0]]
            if self.droite:
                result += self.droite.infixe()
            return result
        
    def postfixe(self):
        if self.estVide():
            return 0
        else:
            result = []
            if self.gauche:
                result += self.gauche.postfixe()
            if self.droite:
                result += self.droite.postfixe()
            result += [self.racine[0]]
            return result
        
    def hauteur(self):
        if self.estVide():
            return -1
        else:
            h_gauche = self.gauche.hauteur() if self.gauche is not None else -1
            h_droite = self.droite.hauteur() if self.droite is not None else -1
            return 1 + max(h_gauche, h_droite)
        # if self.gauche is None and self.droite is None:
        #     return -1
        # else:
        #     return 1 + max(self.gauche.hauteur(), self.droite.hauteur())
        
    def estABR(self):
        if self.estVide():
            return True
        else:
            if self.gauche and self.gauche.racine[0] > self.racine[0]:
                return False
            if self.droite and self.droite.racine[0] < self.racine[0]:
                return False
            if self.gauche and not self.gauche.estABR():
                return False
            if self.droite and not self.droite.estABR():
                return False
            return True

    
    def estEquilibre(self):
        if self.estVide():
            return True
        else:
            delta = 0
            gauche = self.gauche.hauteur() if self.gauche is not None else -1
            droite = self.droite.hauteur() if self.droite is not None else -1
            delta = gauche - droite
            if delta > 1 or delta < -1:
                return False
            else:
                gauche = self.gauche.estEquilibre() if self.gauche is not None else True
                droite = self.droite.estEquilibre() if self.droite is not None else True
                return True and gauche and droite
            
    def rotation_droite(self):
        if self.gauche is None:
            return self

        new_root = self.gauche
        self.gauche = new_root.droite
        new_root.droite = self
        return new_root    

    def rotation_gauche(self):
        if self.droite is None:
            return self

        new_root = self.droite
        self.droite = new_root.gauche
        new_root.gauche = self
        return new_root
    
N5 = AB(8)    
N4 = AB(12)
N3 = AB(3)
N2 = AB(5, N3, N5)
N1 = AB(10, N2, N4)
# N1 = AB()
test = N1


# test.afficher()
# print("taille de l'arbre :", test.taille())
# print("Parcours préfixe :", test.prefixe())
# print("Parcours infixe :", test.infixe())
# print("Parcours postfixe :", test.postfixe())
print("Hauteur de l'arbre:", test.hauteur())
# print("Est-ce que l'arbre est un ABR?", test.estABR())
# print("Est-ce que l'arbre est équilibré?", test.estEquilibre())


#corriger hauteur si il est vide = -1
# N3 = AB(11)
# N2 = AB(5)
# N1 = AB(10, N2, N3)
# test = N1
# test.afficher()
# print("tototototootototototototo")
# test = test.rotation_gauche()
# test.afficher()