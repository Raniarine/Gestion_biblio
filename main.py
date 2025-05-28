from Bibliotheque import Bibliotheque

def menu():
    print("\n********* MENU BIBLIOTHÈQUE **********")
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
            isbn = input("ISBN : ")
            biblio.ajouter_livre(titre, auteur, isbn)

        elif choix == "2":
            nom = input("Nom : ")
            identifiant = input("Identifiant : ")
            biblio.enregistrer_utilisateur(nom, identifiant)

        elif choix == "3":
            print("Liste des livres disponibles :")
            biblio.lister_livres(uniquement_disponibles=True)

        elif choix == "4":
            identifiant = input("Identifiant utilisateur : ")
            isbn = input("ISBN du livre : ")
            biblio.emprunter_livre(identifiant, isbn)

        elif choix == "5":
            identifiant = input("Identifiant utilisateur : ")
            isbn = input("ISBN du livre : ")
            biblio.rendre_livre(identifiant, isbn)

        elif choix == "6":
            biblio.afficher_utilisateurs()

        elif choix == "7":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
