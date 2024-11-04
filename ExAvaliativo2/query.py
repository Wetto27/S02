from database import Database

class Query:
    def __init__(self):
        self.db = Database("bolt://3.236.155.114:7687", "neo4j", "location-bristle-compensation")

    def close(self):
        self.db.close()

    def query_Q1_a(self):
        query = """
        MATCH (t:Teacher {name: 'Renzo'})
        RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        results = self.db.execute_query(query)
        return results

    def query_Q1_b(self):
        query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name AS name, t.cpf AS cpf
        """
        results = self.db.execute_query(query)
        return results

    def query_Q1_c(self):
        query = """
        MATCH (c:City)
        RETURN c.name AS name
        """
        results = self.db.execute_query(query)
        return results

    def query_Q1_d(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS name, s.address AS address, s.number AS number
        """
        results = self.db.execute_query(query)
        return results

    def query_Q2_a(self):
        query = """
        MATCH (t:Teacher)
        RETURN MIN(t.ano_nasc) AS oldest_birth_year, MAX(t.ano_nasc) AS youngest_birth_year
        """
        results = self.db.execute_query(query)
        return results

    def query_Q2_b(self):
        query = """
        MATCH (c:City)
        RETURN AVG(c.population) AS average_population
        """
        results = self.db.execute_query(query)
        return results

    def query_Q2_c(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN REPLACE(c.name, 'a', 'A') AS city_name
        """
        results = self.db.execute_query(query)
        return results

    def query_Q2_d(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 2, 1) AS third_letter
        """
        results = self.db.execute_query(query)
        return results

if __name__ == "__main__":
    query = Query()
    
    print("Questao 1 - A:")
    print(query.query_Q1_a())
    print()

    print("Questao 1 - B:")
    print(query.query_Q1_b())
    print()
    
    print("Questao 1 - C:")
    print(query.query_Q1_c())
    print()
    
    print("Questao 1 - D:")
    print(query.query_Q1_d())
    print()
    
    print("Questao 2 - A:")
    print(query.query_Q2_a())
    print()
    
    print("Questao 2 - B:")
    print(query.query_Q2_b())
    print()
    
    print("Questao 2 - C:")
    print(query.query_Q2_c())
    print()
    
    print("Questao 2 - D:")
    print(query.query_Q2_d())
    print()
    
    query.close()