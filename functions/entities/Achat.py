# Exemple d'utilisation :
# paniers = {"Client1": [(1, 2), (2, 3)], "Client2": [(1, 1)]}
# produits_disponibles = [(1, "Produit A", "2$"), (2, "Produit

class AnalyseAchats:
    def __init__(self, paniers, produits_disponibles):
        """
        paniers: dict {nom_client: [(id_produit, quantité), ...]}
        produits_disponibles: list of tuples (id_produit, nom, prix)
        """
        self.paniers = paniers
        # Convertir en dict {id_produit: (nom, prix_float)}
        self.produits_dic = {
            id_: (nom, float(prix.replace('$', '')) if isinstance(prix, str) else float(prix))
            for id_, nom, prix in produits_disponibles
        }

    def produits_plus_achetes(self, top_n=5):
        """
        Retourne une liste de tuple (nom_produit, quantité_totale) des produits les plus achetés.
        """
        compteur = {}
        for panier in self.paniers.values():
            for id_produit, quantite in panier:
                compteur[id_produit] = compteur.get(id_produit, 0) + quantite

        produits_tries = sorted(compteur.items(), key=lambda x: x[1], reverse=True)
        resultats = []
        for id_produit, quantite in produits_tries[:top_n]:
            nom = self.produits_dic.get(id_produit, ("Produit inconnu", 0))[0]
            resultats.append((nom, quantite))
        return resultats

