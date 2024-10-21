from database import Database

class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (:Player {player_id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    def update_player(self, player_id, new_name):
        query = "MATCH (p:Player {player_id: $player_id}) SET p.name = $new_name"
        parameters = {"player_id": player_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.player_id AS player_id, p.name AS name"
        results = self.db.execute_query(query)
        return [(result["player_id"], result["name"]) for result in results]

    def create_match(self, match_id, player_ids, results):
        query = """
        CREATE (m:Match {match_id: $match_id})
        WITH m
        UNWIND $player_ids AS player_id
        MATCH (p:Player {player_id: player_id})
        CREATE (p)-[:PARTICIPATED {result: $results[player_id]}]->(m)
        """
        parameters = {"match_id": match_id, "player_ids": player_ids, "results": results}
        self.db.execute_query(query, parameters)

    def get_match(self, match_id):
        query = """
        MATCH (m:Match {match_id: $match_id})<-[r:PARTICIPATED]-(p:Player)
        RETURN m.match_id AS match_id, p.player_id AS player_id, p.name AS player_name, r.result AS result
        """
        parameters = {"match_id": match_id}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"], result["player_id"], result["player_name"], result["result"]) for result in results]

    def get_player_matches(self, player_id):
        query = """
        MATCH (p:Player {player_id: $player_id})-[r:PARTICIPATED]->(m:Match)
        RETURN m.match_id AS match_id, p.player_id AS player_id, p.name AS player_name, r.result AS result
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [(result["match_id"], result["player_id"], result["player_name"], result["result"]) for result in results]

    def delete_match(self, match_id):
        query = "MATCH (m:Match {match_id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)