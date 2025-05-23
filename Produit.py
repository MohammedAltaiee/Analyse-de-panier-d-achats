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
        # self._produits = produits if produits is not None else []  # Use a private attribute

    class Item(BaseModel):
        id: int
        nom: str
        prix: float
    
    # @property
    # def produits(self):
    #     return self._produits

    # @produits.setter
    # def produits(self, value):
    #     if not isinstance(value, list):
    #         raise ValueError("Produits doit etre une liste de tuples.")
    #     # You might add further validation here, e.g., checking the tuple structure
    #     self._produits = value

    # def prix(self, id_produit: int) -> float | None:
    #     for p in self.produits:
    #         if p[0] == id_produit:
    #             return p[2]
    #     return None
    
    # def nom(self, id_produit: str)-> str | None:
    #     for p in self.produits:
    #         if p[0] == id_produit:
    #             return p[1]
    #     return None
    

    # Methode pour ajouter un produit d'un fichier csv avec
    #  ID,Product,Unit Price (CAD)
    # 1,Alcool à Friction (bouteille de 500ml),$4.00
    def ajouter_produits_depuis_csv(self, chemin_csv: str):
        try:
            with open(chemin_csv, mode='r', encoding='utf-8') as fichier:
                lecteur = csv.DictReader(fichier)
                for ligne in lecteur:
                    id_produit = int(ligne['ID'])
                    nom_produit = ligne['Product']
                    prix_str = ligne['Unit Price (CAD)'].replace('$', '').replace(',', '.').strip()
                    prix_produit = float(prix_str)
                    ajouter_produit(id_produit, nom_produit, prix_produit)
        except Exception as e:
            print(f"Erreur lors de l'ajout des produits depuis le CSV : {e}")



    def ajouter_produit_tuple(self, id_produit, nom_produit, prix_produit):
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
    
    def ajouter_produit(self, nom_produit, prix_produit):
        """
        (nom, prix)
        puis on cree un nouvel id so nom est nouveau
        """

        # Verification de l'existence de nom dans produits
        # for p in self.produits:
        #     if p[1] == ProduitEntite.canoniser_nom(nom_produit):
        #         raise ValueError("Le produit existe déjà).")
        if self.rechercher_produit(nom_produit) != None:
            raise ValueError("Le produit existe déjà.")
        
        nouveau_id = max([p[0] for p in self.produits]) + 1
        self.produits.append((nouveau_id, ProduitEntite.canoniser_nom(nom_produit), prix_produit))

    def maj_produit_par_id(self, id_produit, nouveau_nom_produit, nouveau_prix_produit):
        self.produits[id_produit].nom = nouveau_nom_produit
        self.produits[id_produit].prix = nouveau_prix_produit
        # self.produits[id_produit] = (id_produit, nouveau_nom_produit, nouveau_prix_produit)
    
    def maj_produit_nom_par_id(self, id_produit, nouveau_nom_produit):
        self.produits[id_produit].nom = nouveau_nom_produit

    def supprimer_produit_par_id(self, id_produit):
        """
        Supprime un  produit  par ID.
        """
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


    # Utilitaires
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
        "lampe-de-bureau" -> "Lampe-de-bureau"
        """
        return nom_produit.capitalize().replace(" ", "_") #.replace("-", "__")

    def imprimer(self):
        for p in self.produits:
            print(p)

    def afficher(self):
        return json.dumps(self.produits)

    # utilitaire classe Python
    
    def __str__(self):
        return self.afficher()

    def __repr__(self):
        return self.afficher()
    
    def __len__(self):
        return len(self.produits)
    
    def __getitem__(self, index: int):
        return self.produits[index]

    # def __getitem__(self, name: str):
    #     return self.rechercher_produit(name)
    
    # def __setitem__(self, index, prod: Tuple[int, str, float]):
    #     self.produits[index] = prod
    
    # def __setitem__(self, name, prod_name: str):
    #     prod = self.rechercher_produit(prod_name)
    #     if prod == None:
    #         raise ValueError("Le produit n'existe pas.")
    #     self.produits[name] = prod
    

    # def __delitem__(self, index):
    #     del self.produits[index]
    
    # def __iter__(self):
    #     return iter(self.produits)
    
    # def __contains__(self, item):
    #     return item in self.produits