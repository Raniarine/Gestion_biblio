class Utilisateur:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté le livre '{livre.get_titre()}'.")
        else:
            print(f"Le livre '{livre.get_titre()}' n'est pas disponible.")

    def rendre_livre(self, isbn):
        for livre in self.livres_empruntes:
            if livre.get_isbn() == isbn:
                livre.retourner()
                self.livres_empruntes.remove(livre)
                print(f"{self.nom} a rendu le livre '{livre.get_titre()}'.")
                return
        print("Livre non trouvé dans les emprunts.")

    def afficher_livres(self):
        if not self.livres_empruntes:
            print(f"{self.nom} n'a emprunté aucun livre.")
        else:
            print(f"Livres empruntés par {self.nom} :")
            for livre in self.livres_empruntes:
                livre.afficher_info()
