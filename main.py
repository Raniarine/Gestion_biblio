from livre import Livre
from utilisateur import Utilisateur
from bibliotheque import Bibliotheque

def menu():
    print("\n***** MENU BIBLIOTHÈQUE *****")
    print("1. Ajouter un livre")
    print("2. Inscrire un utilisateur")
    print("3. Lister les livres")
    print("4. Emprunter un livre")
    print("5. Rendre un livre")
    print("6. Afficher les utilisateurs")
    print("7. Quitter")

def main():
    biblio = Bibliotheque()
    while True:
        menu()
        choix = input("Choix : ")
        if choix == "1":
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            livre = Livre(titre, auteur)
            biblio.ajouter_livre(livre)
        elif choix == "2":
            nom = input("Nom : ")
            identifiant = input("Identifiant : ")
            utilisateur = Utilisateur(nom, identifiant)
            biblio.ajouter_utilisateur(utilisateur)
        elif choix == "3":
            biblio.lister_livres(uniquement_disponibles=True)
        elif choix == "4":
            nom_user = input("Nom utilisateur : ")
            titre = input("Titre du livre : ")
            # trouver et emprunter
            for u in biblio.utilisateurs:
                if u.nom == nom_user:
                    for l in biblio.livres:
                        if l.get_titre() == titre:
                            u.emprunter_livre(l)
                            break
                    break
        elif choix == "5":
            nom_user = input("Nom utilisateur : ")
            titre = input("Titre du livre : ")
            for u in biblio.utilisateurs:
                if u.nom == nom_user:
                    u.rendre_livre(titre)
                    break
        elif choix == "6":
            biblio.afficher_utilisateurs()
        elif choix == "7":
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
