class MotoristaDAO:
    def __init__(self, database):
        self.db = database
        self.collection = self.db.get_collection()

    def create_motorista(self, motorista):
        result = self.collection.insert_one(motorista.to_dict())
        return result.inserted_id

    def read_motorista(self, motorista_id):
        return self.collection.find_one({"_id": motorista_id})

    def update_motorista(self, motorista_id, novos_valores):
        result = self.collection.update_one({"_id": motorista_id}, {"$set": novos_valores})
        return result.modified_count

    def delete_motorista(self, motorista_id):
        result = self.collection.delete_one({"_id": motorista_id})
        return result.deleted_count