from database import Database
from game_database import GameDatabase

db = Database("bolt://3.235.136.19:7687", "neo4j", "dears-finger-interpreters")
db.drop_all()

game_db = GameDatabase(db)

game_db.create_player("player1", "Anna")
game_db.create_player("player2", "Lucas")
game_db.create_player("player3", "Gabriel")

game_db.create_match("match1", ["player1", "player2"], {"player1": 7, "player2": 6})
game_db.create_match("match2", ["player2", "player3"], {"player2": 10, "player3": 3})
game_db.create_match("match3", ["player1", "player3"], {"player1": 8, "player3": 9})

game_db.update_player("player2", "Camille")

game_db.delete_match("match3")

print("Jogadores:")
print(game_db.get_players())
print("Partida 1:")
print(game_db.get_match("match1"))
print("Partidas de Anna:")
print(game_db.get_player_matches("player1"))

db.close()