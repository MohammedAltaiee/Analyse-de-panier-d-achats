# 3.
# 3.1. Fonction pour ajouter un produit dans un panier
def ajouter_produit_panier(dic, client, id_produit, quantite):
    produit = (id_produit, quantite)
    if client in dic:
      dic[client].append(produit)
      print(f"Produit {produit} ajouté au panier de '{client}'.")
    else:
      dic[client] = [produit]
      print(f"Nouveau client '{client}' créé avec le produit {produit}.")

# Example: ajouter le produit (4, 10) au panier de Anne Alyst
ajouter_produit_panier(dic_exemple, "Anne Alyst", 4, 10)
print(dic_exemple["Anne Alyst"])

# 3.2. Fonction pour supprimer un produit d'un panier
def supprimer_produit_panier(dic, client, id_produit):
    if client in dic_exemple:
        panier = dic_exemple[client]
        dic_exemple[client] = [item for item in panier if item[0] != id_produit]
        print(f"Produit {id_produit} retiré du panier de {client}.")
    else:
        print(f"Le client {client} n'a pas de panier.")

# Example: supprimer le produit 4 au panier de Anne Alyst
supprimer_produit_panier(dic_exemple,"Anne Alyst", 4)
print(dic_exemple["Anne Alyst"])

# 4. Fonction pour calculer le total du panier
def calculer_total_panier(dic, client, produits):
    if client not in dic:
      print(f"Client '{client}' non trouvé.")
      return 0
    total = 0.0
    panier = dic[client]
    for id_panier, quantite in panier:
        for id_prod, nom, prix in produits:
            if id_prod == id_panier:
               if isinstance(prix, str):
                    prix = float(prix.replace("$", "").strip())
               total += prix * quantite
               break

    return round(total, 2)

# Example: calculer le total pour un client
total = calculer_total_panier(dic_exemple, "Anne Alyst", produits)
print(f"Total du panier de Anne Alyst : {total} CAD")
#14+21

# 5. Fonction pour afficher le contenu du panier
def afficher_contenu_panier(dic, client, produits):
    if client not in dic:
        print(f"Client '{client}' non trouvé.")
        return
    print(f"Contenu du panier de '{client}':")
    panier = dic[client]
    total = 0.0

    for id_panier, quantite in panier:
        for id_prod, nom, prix in produits:
            if id_prod == id_panier:
                print(f"Quantité: {quantite}, {nom}")
                break

# Example: le contenu du panier de "Anne Alyst"
afficher_contenu_panier(dic_exemple, "Anne Alyst", produits)