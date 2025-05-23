# create a simple tui that loads ./data/panier.json and ./data/produits.json

import json
import os
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

import Produit
# import ProduitEntite.Item




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
# async def test_tout_produits_post(payload: Produit.ProduitEntite.Item):
#     p = Produit.ProduitEntite.Item()
#     p.id = 12345
#     p.nom = "whatwaaaa"
#     p.prix = 3.1415
#     print("P::: " + p)
#     print("PAYLOAD::: " + payload)
#     return {"testing": p}

# @app.post("/test/produits")
# async def test_tout_produits_post_text(params: Produit.ProduitEntite.ProduitType):
#     print(str(params))
#     return {"testing": str(params)}

class ItemPayload(BaseModel):
    id: int
    nom: str
    prix: float

class RequestBody(BaseModel):
    payload: ItemPayload


@app.post("/test/produits")
async def test_tout_produits_post(request_body):
    item_data  = query.payload
    print(f"Received item: {item_data}")
    return {"testing": item_data}


def main():
    produits = Produit.ProduitEntite([])
    # produits.ajouter_produits_depuis_csv("./data/produits.csv")

    produits.imprimer()


if __name__ == "__main__":
    main()

# 
