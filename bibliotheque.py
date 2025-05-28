from livre import Livre
from utilisateur import Utilisateur

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print("Livre ajouté avec succès.")

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)
        print("Utilisateur ajouté avec succès.")

    def lister_livres(self, uniquement_disponibles=False):
        for livre in self.livres:
            if not uniquement_disponibles or livre.est_disponible():
                livre.afficher_info()

    def afficher_utilisateurs(self):
        for utilisateur in self.utilisateurs:
            print(f"Nom: {utilisateur.nom}, ID: {utilisateur.identifiant}")
            utilisateur.afficher_livres()
