class Livre:
    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
        self._disponible = True

    def afficher_info(self):
        statut = "Disponible" if self._disponible else "Emprunté"
        print(f"Titre: {self._titre}, Auteur: {self._auteur}, Statut: {statut}")

    def emprunter(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def retourner(self):
        self._disponible = True

    def est_disponible(self):
        return self._disponible

    def get_titre(self):
        return self._titre

    def get_auteur(self):
        return self._auteur
