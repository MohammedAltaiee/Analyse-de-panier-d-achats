class ClientEntite:
    def __init__(self, nom, email=None):
        self.nom = nom.capitalize()        
        self.id = self.nom.hash()

    def __repr__(self):
        return f"Client(ID='{self.id}', nom='{self.nom}')"

    def get_nom(self):
        return self.nom

    def get_id(self):
        return self.id
    
    def code_client(self):
        """
        Retourne le code client sous la forme 'ID09876', 'ID0123452', etc.
        """
        return f"ID{self.id}"
    
    @staticmethod
    def nom_canonique(nom: str):
        """
        Retourne le nom canonique sous la forme de Prenom_Nom.
        """
        return nom.capitalize().replace(" ", "_")