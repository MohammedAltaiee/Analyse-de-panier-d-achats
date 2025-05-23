# create a simple tui that loads ./data/panier.json and ./data/produits.json

import json
import os
from typing import List
from fastapi import FastAPI

import Produit

test_produits = Produit.ProduitEntite([])
test_produits.ajouter_produits_depuis_csv("./data/produits.csv")

app = FastAPI()

@app.get("/bonjour")
async def root_bonjour():
    return {"message": "Bonjour Hello la classe NPower QC 2025 "}

@app.get("/test/produits")
async def test_tout_produits_get():
    return test_produits.afficher()

# @app.post("/test/produits")
# async def test_tout_produits_post(params: Produit.ProduitEntite.ProduitType):
#     print(params)
#     return {"testing": params}

@app.post("/test/produits")
async def test_tout_produits_post_text(params: str):
    print(params)
    return {"testing": params}





def main():
    produits = Produit.ProduitEntite([])
    # produits.ajouter_produits_depuis_csv("./data/produits.csv")

    produits.imprimer()


if __name__ == "__main__":
    main()

# 
