import csv
import json
from typing import Tuple
from pydantic import BaseModel

# Exemple d'utilisation :
# produits = [(1, "ampoules (del, unité)", 2.5), (2, "lampe", 10)]
# pm = ProduitEntite(produits)
# resultat = pm.rechercher_produit("ampoules (del, unité)")
# print(resultat)

class ProduitEntite:
    def __init__(self, produits):
        # produits: list of tuples (id, nom, prix)
        # type: [(int, str, float)]
        self.produits = produits

    class ProduitType(BaseModel):
        id: int | None = None
        nom: str
        prix: float


    # Methode pour ajouter un produit d'un fichier csv avec
    #  ID,Product,Unit Price (CAD)
    # 1,Alcool à Friction (bouteille de 500ml),$4.00
    def ajouter_produits_depuis_csv(self, chemin_csv):
        try:
            with open(chemin_csv, mode='r', encoding='utf-8') as fichier:
                lecteur = csv.DictReader(fichier)
                for ligne in lecteur:
                    id_produit = int(ligne['ID'])
                    nom_produit = ligne['Product']
                    prix_str = ligne['Unit Price (CAD)'].replace('$', '').replace(',', '.').strip()
                    prix_produit = float(prix_str)
                    self.ajouter_produit(id_produit, nom_produit, prix_produit)
        except Exception as e:
            print(f"Erreur lors de l'ajout des produits depuis le CSV : {e}")



    def ajouter_produit(self, id_produit, nom_produit, prix_produit):
        # Verification des types
        # id_produit: int
        # nom_produit: str
        # prix_produit: float
        if not isinstance(id_produit, int) or not isinstance(nom_produit, str) or not isinstance(prix_produit, (int, float)):
            raise ValueError("Les types des arguments ne sont pas valides.")
        # Verification de la validité du prix
        if prix_produit < 0:
            raise ValueError("Le prix du produit ne peut pas être négatif.")
        # ajouter ou ecraser/maj le produit
        self.produits.append((id_produit, ProduitEntite.canoniser_nom(nom_produit), prix_produit))

    def supprimer_produit_par_id(self, id_produit):
        """
        Supprime un  produit  par ID."""
        # verification de type
        # id_produit: int
        if not isinstance(id_produit, int):
            raise ValueError("L'ID du produit doit être un entier.")
        # Suppression du  produit 
        for i, p in enumerate(self.produits):
            if p[0] == id_produit:
                del self.produits[i]
                return
        # ou bien self.produits = [p for p in self.produits if p[0] != id_produit]
    
    def supprimer_produit_par_nom(self, nom_produit):
        """
        Supprime un  produit  par nom."""
        # verification de type
        # nom_produit: str
        if not isinstance(nom_produit, str):
            raise ValueError("L'ID du produit doit être un entier.")
        # Suppression du  produit 
        for i, p in enumerate(self.produits):
            if p[1] == ProduitEntite.canoniser_nom(nom_produit):
                del self.produits[i]
                return


    def rechercher_produit(self, nom_produit) -> Tuple[int, str, float] | None:
        """
        Rechercher un  produit  par nom -> ID (type int)
        """
        # verification de type
        # nom_produit: str
        if not isinstance(nom_produit, str):
            raise ValueError("Le nom du produit doit être une chaîne de caractères.")
        # Recherche du produit
        nom_produit = ProduitEntite.canoniser_nom(nom_produit)
        for p in self.produits:
            if p[1] == nom_produit:
                return p  # Retourne le tuple complet (id, nom, prix): (int, str, float)
        return None  # Si le produit n'est pas trouvé
    
    @staticmethod
    def canoniser_nom(nom_produit):
        """
        Retourne le nom du produit sous la forme canonique.
        Exemples : 
        "ampoules DEL" -> "Ampoules_Del"
        "lampe" -> "Lampe"
        "lampe-de-bureau" -> "Lampe__de__bureau"
        """
        return nom_produit.capitalize().replace(" ", "_").replace("-", "__")

    def imprimer(self):
        for p in self.produits:
            print(p)

    def afficher(self):
        return json.dumps(self.produits)
    

