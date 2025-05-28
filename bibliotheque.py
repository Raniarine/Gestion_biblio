from Livre import Livre
from Utilisateur import Utilisateur

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print("Livre ajouté avec succès.")

    def enregistrer_utilisateur(self, nom, identifiant):
        utilisateur = Utilisateur(nom, identifiant)
        self.utilisateurs.append(utilisateur)
        print("Utilisateur enregistré.")

    def lister_livres(self, uniquement_disponibles=False):
        for livre in self.livres:
            if not uniquement_disponibles or livre.est_disponible():
                livre.afficher_info()

    def trouver_livre(self, isbn):
        for livre in self.livres:
            if livre.get_isbn() == isbn:
                return livre
        return None

    def trouver_utilisateur(self, identifiant):
        for utilisateur in self.utilisateurs:
            if utilisateur.identifiant == identifiant:
                return utilisateur
        return None

    def emprunter_livre(self, identifiant, isbn):
        utilisateur = self.trouver_utilisateur(identifiant)
        livre = self.trouver_livre(isbn)
        if utilisateur and livre:
            utilisateur.emprunter_livre(livre)
        else:
            print("Utilisateur ou livre non trouvé.")

    def rendre_livre(self, identifiant, isbn):
        utilisateur = self.trouver_utilisateur(identifiant)
        if utilisateur:
            utilisateur.rendre_livre(isbn)
        else:
            print("Utilisateur non trouvé.")

    def afficher_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(f"Nom: {utilisateur.nom}, ID: {utilisateur.identifiant}")
            utilisateur.afficher_livres()
