# create a simple tui that loads ./data/panier.json and ./data/produits.json

import json
import os
import logging
from typing import List
from flask import Flask, request, jsonify
from pydantic import BaseModel

import Produit
# import ProduitEntite.Item

# Configure logging (usually done once at the beginning of your script)
logging.basicConfig(level=logging.DEBUG,  # Set the minimum level to capture
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='app.log',  # Optional: log to a file
                    filemode='w')  # Optional: overwrite the log file each time

# Create a logger for your module (or use the root logger)
logger = logging.getLogger(__name__)  # Or logging.getLogger('my_app')



app = Flask(__name__)

test_produits = Produit.ProduitEntite([])
# test_produits.ajouter_produits_depuis_csv("./data/produits.csv")

# global prods  # Declare produits as global to modify it
# prods = Produit.ProduitEntite([(0, "Le_Savoir", 0)])
# # prods = Produit.ProduitEntite([(0, "Le_Savoir", 0)])
# # produits.ajouter_produits_depuis_csv("./data/produits.csv")
# prods.ajouter_produit_tuple(id_produit=0, nom_produit="Le_Savoir", prix_produit=0)
# print(prods)
# logger.debug("Debut script, Debug message: {prods}")


@app.route('/bonjour', methods=['GET'])
def root_bonjour():    
    res = {"message": "Bonjour par default :) Hello la classe NPower QC 2025."}
    logger.debug("HIT root_bonjour(): {prods}")
    if prods.produits[0] == (0, "Le_Savoir", 0):
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

    # # Configure logging (usually done once at the beginning of your script)
    # logging.basicConfig(level=logging.DEBUG,  # Set the minimum level to capture
    #                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #                 filename='app.log',  # Optional: log to a file
    #                 filemode='w')  # Optional: overwrite the log file each time

    # # Create a logger for your module (or use the root logger)
    # logger = logging.getLogger(__name__)  # Or logging.getLogger('my_app')


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
    prods = Produit.ProduitEntite([(0, "Le_Savoir", 0)])
    # prods.ajouter_produits_depuis_csv("./data/produits.csv")
    # prods.ajouter_produit_tuple(id_produit=0, nom_produit="Le_Savoir", prix_produit=0)
    # prods.ajouter_produit_tuple(id_produit=0, nom_produit="Le_Savoir", prix_produit=0)
    logger.info("MAIN Debug message: {prods}")
    
    print("Produits charges.")

if __name__ == "__main__":
    main()
    app.run(host='0.0.0.0', port=80, debug=True)  # Start the Flask development server

# 
