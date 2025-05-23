# create a simple tui that loads ./data/panier.json and ./data/produits.json

import json
import os


import Produit

produits = Produit.ProduitEntite([])

def main():
    produits = Produit.ProduitEntite([])
    produits. ajouter_produits_depuis_csv("./data/produits.csv")

    produits.afficher()


if __name__ == "__main__":
    main()

# 
