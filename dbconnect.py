import mysql.connector
from mysql.connector import Error

class Connection:

    def __init__(self) -> None:
        """
           Constructeur de la class Connection qui initialise les parametres de connection
           a la base de donnee 
        """
        self.host = 'localhost'
        self.database = 'paryaj'
        self.user = 'root'
        self.password = ''
        self.con = None

    def __enter__(self):
        """
            function Qui etablie le connection automatiquement avec la base de donnee
            a utiliser avec le mot Cles WITH
        """
        try:
            self.con = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return self.con
        except Error as err:
            err= "Error while connecting to MySQL :" + err
            return err

    def __exit__(self, exc_type, exc_value, traceback):
        """
            fonction qui ferme la connection auomatiquement que l'on sorte du bloc 
            WITH. il est utiliser pour eviter d'appeler a chaque fois la methode close()
            pour fermer la connection a la base de donnees. 
        """
        if self.con and self.con.is_connected():
            self.con.close()