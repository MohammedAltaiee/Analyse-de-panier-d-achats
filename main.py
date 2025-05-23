# create a simple tui that loads ./data/panier.json and ./data/produits.json

import json
import os
from typing import List
from flask import Flask, request, jsonify
from pydantic import BaseModel

import Produit
# import ProduitEntite.Item




# test_produits = Produit.ProduitEntite([])
# test_produits.ajouter_produits_depuis_csv("./data/produits.csv")

app = Flask(__name__)

@app.route('/bonjour', methods=['GET'])
def root_bonjour():
    return jsonify({"message": "Bonjour Hello la classe NPower QC 2025"})


# @app.get("/bonjour")
# async def root_bonjour():
#     return {"message": "Bonjour Hello la classe NPower QC 2025 "}

# @app.get("/test/produits")
# async def test_tout_produits_get():
#     return test_produits.afficher()

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

# class ItemPayload(BaseModel):
#     id: int
#     nom: str
#     prix: float

# class RequestBody(BaseModel):
#     payload: ItemPayload


# @app.post("/test/produits")
# async def test_tout_produits_post(request_body):
#     item_data : ItemPayload =  request_body.payload
#     print(f"Received item: {item_data}")
#     return {"testing": item_data}


class ItemPayload(BaseModel):
    id: int
    nom: str
    prix: float


@app.route('/test/produits', methods=['POST'])
def test_tout_produits_post():
    try:
        data = request.get_json()
        if not data or 'payload' not in data:
            return jsonify({"error": "Invalid payload"}), 400

        item_data = ItemPayload(**data['payload'])  # Validate and parse with Pydantic
        print(f"Received item: {item_data}")
        return jsonify({"testing": item_data.dict()})  # Return as a dictionary

    except Exception as e:
        return jsonify({"error": str(e)}), 400


def main():
    produits = Produit.ProduitEntite([])
    # produits.ajouter_produits_depuis_csv("./data/produits.csv")
    produits.imprimer()

    # The Flask app handles requests, so this part is less relevant now.
    # You might still want to initialize things here if needed.
    # For example, if you want to load products at startup:
    # global produits  # Declare produits as global to modify it
    # produits = Produit.ProduitEntite([])
    # produits.ajouter_produits_depuis_csv("./data/produits.csv")
    # print("Produits loaded.")
    pass  # Or any other initialization

if __name__ == "__main__":
    main()
    app.run(debug=True)  # Start the Flask development server

# 
