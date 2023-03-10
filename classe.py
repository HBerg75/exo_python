from datetime import date

class Commande:
    def __init__(self, numero, prix=0):
        self.numero = numero
        self.date = date.today()
        self.prix = prix
    
    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero
    
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date
    
    def get_prix(self):
        return self.prix
    
    def set_prix(self, prix):
        self.prix = prix
    
    def calculTVA(self):
        return self.prix * 0.196
    
    def acquitter(self):
        return CommandeAcquittee(self.numero, self.prix)

    def __add__(self, other):
        numero = max(self.numero, other.numero) + 1
        date = max(self.date, other.date)
        prix = self.prix + other.prix
        return Commande(numero, prix)

    def __str__(self):
        return f"Commande {self.numero} du {self.date} d'un montant de {self.prix} euros"


class Client:
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
    
    def get_nom(self):
        return self.nom
    
    def set_nom(self, nom):
        self.nom = nom
    
    def get_adresse(self):
        return self.adresse
    
    def set_adresse(self, adresse):
        self.adresse = adresse
    
    def contacter(self):
        print(f"{self.nom}\n{self.adresse}")
    
    def __str__(self):
        return f"{self.nom}\n{self.adresse}"


class CommandeAcquittee(Commande):
    def __init__(self, numero, prix=0, date_paiement=None):
        super().__init__(numero, prix)
        self.date_paiement = date_paiement
    
    def get_date_paiement(self):
        return self.date_paiement
    
    def set_date_paiement(self, date_paiement):
        self.date_paiement = date_paiement
    
    def acquitter(self):
        return self
    
    def __str__(self):
        if self.date_paiement:
            return f"Commande {self.numero} du {self.date} d'un montant de {self.prix} euros, payée le {self.date_paiement}"
        else:
            return f"Commande {self.numero} du {self.date} d'un montant de {self.prix} euros, non acquittée"



c1 = Commande(1, 100)
c2 = Commande(2, 200)
print(c1)
print(c2)

c3 = c1 + c2
print(c3)

cl1 = Client("Jean Dupont", "15 rue des Fleurs, 75001 Paris")
cl1.contacter()

ca1 = c1.acquitter()
print(ca1)

ca2 = CommandeAcquittee(2, 200, date.today())
print(ca2)
 