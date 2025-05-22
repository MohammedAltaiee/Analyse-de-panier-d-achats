# 6. Fonction pour analyser les produits les plus achetés
def analyser_produits_plus_achetes(paniers, produits_disponibles, top_n=5):
  """
  Analyse et retourne les produits les plus achetés, triés par quantité décroissante.

  Input: paniers(dict {nom_client: [(id_produit, quantité), ...]});
          produits_disponibles(dict {id_produit: (nom, prix)});
          top_n: nombre de produits à retourner

  Output: Retourne une liste de tuple(nom_produit, quantité_totale) des produits les plus achetés et leur quantité
  """
  # changer la structure de donnée en dictionnaire
  produits_dic = {id_: (nom, float(prix.replace('$', ''))) for id_, nom, prix in produits_disponibles}
  # Créer un dictionnaire pour compter la quantité totale achetée pour chaque produit
  compteur = {}

  # Parcourir tous les paniers de tous les clients
  for panier in paniers.values():
      # Parcourir chaque produit dans le panier
      for id_produit, quantite in panier:
          compteur[id_produit] = compteur.get(id_produit, 0) + quantite

  # Trier les produits par quantité achetée, du plus grand au plus petit
  produits_tries = sorted(compteur.items(), key=lambda x: x[1], reverse=True)

  # Liste pour stocker les résultats finaux
  resultats = []

  # Prendre les top_n premiers produits les plus achetés
  for id_produit, quantite in produits_tries[:top_n]:
      nom = produits_dic.get(id_produit, ("Produit inconnu", 0))[0]
      resultats.append((nom, quantite))

  return resultats