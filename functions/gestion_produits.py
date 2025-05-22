# Fonction pour rechercher les produits
def rechercher_produit(nom_produit):
   # Vérifie que le nom fourni est bien une chaîne de caractères
    if not isinstance(nom_produit, str):
       raise ValueError("Le nom du produit doit être une chaîne de caractères.")
    for p in produits:
        if p[1].lower() == nom_produit.lower():
            return p  # Retourne le tuple complet (id, nom, prix)
    return None  # Si le produit n'est pas trouvé

resultat = rechercher_produit("ampoules (del, unité)")
print(resultat)


