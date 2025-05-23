# create a simple tui that loads ./data/panier.json and ./data/produits.json

import json
import os
from typing import List
from flask import Flask, request, jsonify
from pydantic import BaseModel

import Produit
# import ProduitEntite.Item

app = Flask(__name__)

test_produits = Produit.ProduitEntite([])
test_produits.ajouter_produits_depuis_csv("./data/produits.csv")

global prods  # Declare produits as global to modify it
prods = Produit.ProduitEntite([])
# produits.ajouter_produits_depuis_csv("./data/produits.csv")
prods.ajouter_produit_tuple(id_produit=0, nom_produit="Le_Savoir", prix_produit=0)
print(prods)


@app.route('/bonjour', methods=['GET'])
def root_bonjour():    
    res = {"message": "Bonjour par default :) Hello la classe NPower QC 2025."}
    print(prods)
    if prods.produits[2] == 0:
        res ={"message": "Bonjour Hello la classe NPower QC 2025. Le Savoir n a pas de prix :D"}
    else:
        res ={"message": "Bonjour Hello la classe NPower QC 2025. Le Savoir a un prix :("}
    
    return jsonify(res)


@app.route("/test/produits", methods=["GET"])
def test_tout_produits_get():
    return jsonify(test_produits.afficher())


# class ItemPayload(BaseModel):
#     id: int
#     nom: str
#     prix: float

@app.route('/test/produits', methods=['POST'])
def test_tout_produits_post():
    try:
        data = request.get_json()
        if not data or 'payload' not in data:
            return jsonify({"error": "Invalid payload"}), 400

        # item_data = ItemPayload(**data['payload'])  # Validate and parse with Pydantic
        item_data = Produit.ProduitEntite.Item(**data['payload'])  # Validate and parse with Pydantic

        print(f"Received item: {item_data}")
        return jsonify({"testing": item_data.dict()})  # Return as a dictionary

    except Exception as e:
        return jsonify({"error": str(e)}), 400


def main():
    # produits = Produit.ProduitEntite([])
    # produits.ajouter_produits_depuis_csv("./data/produits.csv")
    # produits.imprimer()

    # test_produits = Produit.ProduitEntite([])
    # test_produits.ajouter_produits_depuis_csv("./data/produits.csv")

    # The Flask app handles requests, so this part is less relevant now.
    # You might still want to initialize things here if needed.
    # For example, if you want to load products at startup:
    # global produits  # Declare produits as global to modify it
    # produits = Produit.ProduitEntite([])
    # produits.ajouter_produits_depuis_csv("./data/produits.csv")
    # print("Produits loaded.")
    # pass  # Or any other initialization

    global prods  # Declare produits as global to modify it
    prods = Produit.ProduitEntite([])
    prods.ajouter_produits_depuis_csv("./data/produits.csv")
    prods.ajouter_produit_tuple(id_produit=0, nom_produit="Le_Savoir", prix_produit=0)
    
    print("Produits charges.")

if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=80, debug=True)  # Start the Flask development server

# 
