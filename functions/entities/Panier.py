# {
#     "Delores Head": [
#         [27, 10],
#         [32, 9],
#         [96, 10],
#         [43, 7]
#     ],
#     "Lou Pole": [
#         [89, 6],
#         [91, 29],
#         [54, 30],
#         [80, 8]
#     ],
#     "Crystal Sight": [
#         [15, 7],
#         [53, 32],
#         [77, 10]
#     ],
# }

# Exemple d'utilisation :
# panier_dic_exemple = {}
# produits = [(1, "Produit A", 2.5), (4, "Produit B", "7$")]
# pm = PanierManager(dic_exemple)
# pm.ajouter_produit("Anne Alyst", 4, 10)
# pm.supprimer_produit("Anne Alyst", 4)
# total = pm.calculer_total("Anne Alyst", produits)
# print(f"Total du panier de Anne Alyst : {total} CAD")
# pm.afficher_contenu("Anne Alyst", produits)

import json

from functions.entities.Client import ClientEntite


class PanierEntite:
    def __init__(self, paniers=None):
        # paniers: dict {client_canonique: [(id_produit, quantite), ...]}
        self.paniers = paniers if paniers is not None else {}

    def panier_depuis_json(self, chemin_json):
        """
        Importe les paniers depuis un fichier JSON.
        Le fichier doit contenir un dictionnaire {client: [[id_produit, quantite], ...]}
        """
        try:
            with open(chemin_json, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Convertir les listes internes en tuples pour cohérence
                self.paniers = {ClientEntite.nom_canonique(client): [tuple(item) for item in produits] for client, produits in data.items()}
            print(f"Paniers importés depuis {chemin_json}")
        except Exception as e:
            print(f"Erreur lors de l'importation des paniers : {e}")


    def ajouter_produit(self, client, id_produit, quantite):
        produit = (id_produit, quantite)
        if client in self.paniers:
            self.paniers[client].append(produit)
            print(f"Produit {produit} ajouté au panier de '{client}'.")
        else:
            self.paniers[client] = [produit]
            print(f"Nouveau client '{client}' créé avec le produit {produit}.")

    def supprimer_produit(self, client, id_produit):
        if client in self.paniers:
            panier = self.paniers[client]
            self.paniers[client] = [item for item in panier if item[0] != id_produit]
            print(f"Produit {id_produit} retiré du panier de {client}.")
        else:
            print(f"Le client {client} n'a pas de panier.")

    def calculer_total(self, client, produits):
        if client not in self.paniers:
            print(f"Client '{client}' non trouvé.")
            return 0
        total = 0.0
        panier = self.paniers[client]
        for id_panier, quantite in panier:
            for id_prod, nom, prix in produits:
                if id_prod == id_panier:
                    if isinstance(prix, str):
                        prix = float(prix.replace("$", "").strip())
                    total += prix * quantite
                    break
        return round(total, 2)

    def afficher_contenu(self, client, produits):
        if client not in self.paniers:
            print(f"Client '{client}' non trouvé.")
            return
        print(f"Contenu du panier de '{client}':")
        panier = self.paniers[client]
        for id_panier, quantite in panier:
            for id_prod, nom, prix in produits:
                if id_prod == id_panier:
                    print(f"Quantité: {quantite}, {nom}")
                    break

