import pymongo
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database: str, collection: str):
        self.connectionString = "mongodb://localhost:27017"
        self.client = pymongo.MongoClient(self.connectionString)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def total_vendas_diario(self):

        pipeline = [
            {
                "$group": {
                    "_id": "$data_compra",
                    "total_vendas": {
                        "$sum": {
                            "$sum": {
                                "$map": {
                                    "input": "$produtos",
                                    "as": "produto",
                                    "in": {"$multiply": ["$$produto.quantidade", "$$produto.preco"]}
                                }
                            }
                        }
                    }
                }
            },
            {"$sort": {"_id": 1}}  # Ordena por data
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "total_vendas_diario")
        return resultado

    def produto_mais_vendido(self):
        pipeline = [
            {
                "$unwind": "$produtos"
            },
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total_vendas": {
                        "$sum": "$produtos.quantidade"
                    }
                }
            },
            {
                "$sort": {"total_vendas": -1}
            },
            {
                "$limit": 1
            }
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "produto_mais_vendido")
        return resultado

    def cliente_que_mais_gastou(self):
        pipeline = [
            {
                "$project": {
                    "cliente_id": "$cliente_id",
                    "total_gasto": {
                        "$sum": {
                            "$map": {
                                "input": "$produtos",
                                "as": "produto",
                                "in": {"$multiply": ["$$produto.quantidade", "$$produto.preco"]}
                            }
                        }
                    }
                }
            },
            {
                "$sort": {"total_gasto": -1}
            },
            {
                "$limit": 1
            }
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "cliente_que_mais_gastou")
        return resultado

    def produtos_vendidos_acima_de_um(self):
        pipeline = [
            {
                "$unwind": "$produtos"
            },
            {
                "$match": {
                    "$expr": {"$gt": ["$produtos.quantidade", 1]}
                }
            },
            {
                "$group": {
                    "_id": "$produtos.descricao",
                    "total_vendas": {
                        "$sum": "$produtos.quantidade"
                    }
                }
            }
        ]
        resultado = list(self.collection.aggregate(pipeline))
        writeAJson(resultado, "produtos_vendidos_acima_de_um")
        return resultado