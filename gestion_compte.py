import mysql.connector
from dbconnect import Connection

class Comptes:

    def __init__(self):
        " Il initialise la variable de class connection qui pointe la class Connection()"
        self.connection = Connection()

    def save_account(self, **compte):
        """
            Enregistre les donnees passer en parametres, il prend une dictionnaire en parametre.
            a utiliser avec le syntaxe suivant : 
            var = Comptes.save_account({'code':'le_code', 'nom':'le_nom' ...})
            le code doit etre une chaine de caractere il n'est pas auto incrementer.
            le champs sexe est enum il prends 'M' OU 'F' . etat : 'A' pour actif, 'S' pour supprimer, 
            'F' pour fermer. et le champs type prends: 'adm' ou 'parieur'
            Quand l'enregistrement est reussi il retourne True . en cas d'echec il retourne False
            et le type d'erreur dans mysql.connector.Error.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    INSERT INTO gestioncompte(code, nom, prenom, sexe, adresse, telephone, nif
                               , nomUser, motDePasse, solde, etat, type)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (compte['code'], compte['nom'], compte['prenom'], compte['sexe'], 
                    compte['adresse'], compte['telephone'], compte['nif'], compte['nom_utilisateur'], 
                    compte['mot_de_passe'], compte['solde'], compte['etat_compte'],
                     compte['type_compte']))
                connect.commit()
                cursor.close()
                return True
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
    
    def modify_account(self,**compte):
        """
        Prends en parametre une dictionnaire , a utiliser comme presenter dans le docString 
        de save_account. il permet de modifier tous les champs d'un compte a part le code.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    UPDATE gestioncompte SET nom = %s, prenom = %s, sexe = %s, adresse = %s, telephone = %s,
                    nif = %s, nomUser = %s , motDePasse = %s, solde, etat, type where code = %s 
                """, (compte['nom'], compte['prenom'], compte['sexe'], compte['adresse'], 
                    compte['telephone'], compte['nif'], compte['nom_utilisateur'], 
                    compte['mot_de_passe'],  compte['solde'], compte['etat_compte'],
                     compte['type_compte'], compte['code']))
                connect.commit()
                cursor.close()
                return True
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
        
    def delete_account(self,code):
       """
        Cette methode Prends en parametre le code du compte a supprimer 
        retour True si la suppression a reussi ou False et le type d'erreur dans une liste 
        quand elle echoue
       """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    DELETE FROM gestioncompte where code = %s 
                """, ( code, ))
                connect.commit()
                cursor.close()
                return True
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
    
    def search_account(self,code):
        """
        Prends en parametre le code du compte le retourne sous la forme d'une liste 
        si il existe dans la table sinon il retour False et le type d'erreur.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    SELECT * FROM gestioncompte where code = %s 
                """, ( code , ))

                compte = cursor.fetchone()
                
                return compte
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
        
    def show_acccounts(self):
        """
        Il retourne une liste de tout les lignes de la table qui forme une liste.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    SELECT * FROM gestioncompte 
                """)

                compte = cursor.fetchall()
                
                return compte
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
