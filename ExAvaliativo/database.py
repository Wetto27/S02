from typing import Collection
import pymongo 

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://root:root@cluster0.tejye.mongodb.net/"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]  # Define a collection corretamente
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def get_collection(self):
        return self.collection  # Adiciona um método para retornar a collection

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)