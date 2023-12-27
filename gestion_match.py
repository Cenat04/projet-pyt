import mysql.connector
import dbconnect


class Matche:


    def __init__(self):
        " Il initialise la variable de class connection qui pointe la class Connection()"
       self.connection = dbconnect.Connection()

    def save_match(self, **match):
         """
            Enregistre les donnees passer de match en parametres, il prend une dictionnaire en parametre.
            a utiliser avec le syntaxe suivant : 
            var = Matche.save_match({'id':'identifiant', 'type_match':'Championnat' ...})
            le code doit etre une chaine de caractere il n'est pas auto incrementer.
            le champs type match prend 'championnat' 'coupe du monde' 'eliminatoire' 'amical'
            et etat prend 'N' pour non encore joue , 'E' pour en cours ,'T' pour terminer,
            'A' pour annuler , 'S' pour supprimer.
            Quand l'enregistrement est reussi il retourne True . en cas d'echec il retourne False
            et le type d'erreur dans mysql.connector.Error.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    INSERT INTO matches( id , typeMatch, paysOuConfederation, dateMatch, heureMatch,
                               equipeReceveuse, equipeVisiteuse, cote, score, etat)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, ( match['Id'], match['typeMatch'], match['pays'], match['date_match'], 
                    match['heure_match'], match['equipe_receveuse'], match['equipeVisiteuse'], match['cote'], 
                    match['score'] , match['etat_match']))
                connect.commit()
                cursor.close()
                return True
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
    
    def modify_match(self, **match):
         """
        Prends en parametre une dictionnaire , a utiliser comme presenter dans le docString 
        de enregistrer_match. il permet de modifier tous les champs d'un compte a part l'Id.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                                UPDATE matches SET typeMatch = %s, paysOuConfederation = %s, dateMatch = %s, heureMatch = %s,
                               equipeReceveuse = %s, equipeVisiteuse = %s, cote  = %s, score = %s, etat = %s where id = %s 
                            """, ( match['typeMatch'], match['pays'], match['date_match'], match['heure_match'], 
                                match['equipe_receveuse'], match['equipeVisiteuse'], match['cote'], 
                                match['score'] , match['etat_match'], match['Id'],))
                connect.commit()
                cursor.close()
                return True
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test

    def delete_match(self, Id):
       """
        Cette methode Prends en parametre l'Id du match a supprimer 
        retour True si la suppression a reussi ou False et le type d'erreur dans une liste 
        quand elle echoue
       """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("DELETE FROM matches where id = %s ", ( Id, ))
                connect.commit()
                cursor.close()
                return True
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
        
    def search_match(self, Id):
      """
        Prends en parametre l'Id du compte le retourne sous la forme d'une liste 
        si il existe dans la table sinon il retour False et le type d'erreur.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                                SELECT * FROM matches where id = %s 
                            """, ( Id, ))

                match = cursor.fetchone()
                
                return match
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
        
    def show_matchs(self):
        """
        Il retourne une liste de tout les lignes de la table qui forme une liste.
        """
        try:
            with self.connection as connect:
                cursor = connect.cursor()
                cursor.execute("""
                    SELECT * FROM matches 
                """)

                matches = cursor.fetchall()
                
                return matches
        except mysql.connector.Error as erreur:
            test = [False , erreur]
            return test
        