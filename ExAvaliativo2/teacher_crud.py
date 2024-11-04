from database import Database

class TeacherCRUD:
    def __init__(self):
        self.db = Database("bolt://3.236.155.114:7687", "neo4j", "location-bristle-compensation")

    def close(self):
        self.db.close()

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        RETURN t
        """
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        results = self.db.execute_query(query, parameters)
        return results

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t
        """
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        RETURN t
        """
        parameters = {"name": name, "newCpf": newCpf}
        results = self.db.execute_query(query, parameters)
        return results