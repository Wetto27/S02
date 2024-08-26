from helper.writeAJson import writeAJson
from database import Database

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def get_all_pokemons(self):
        try:
            result = list(self.database.collection.find({}))
            writeAJson(result, "all_pokemons")
            return result
        except Exception as e:
            print(e)
            return []

    def get_pokemon_by_name(self, name: str):
        try:
            result = self.database.collection.find_one({"name": name})
            writeAJson(result, f"pokemon_{name}")
            return result
        except Exception as e:
            print(e)
            return None

    def get_pokemons_by_type(self, type: str):
        try:
            result = list(self.database.collection.find({"type": type}))
            writeAJson(result, f"pokemons_type_{type}")
            return result
        except Exception as e:
            print(e)
            return []

    def get_pokemons_by_weight(self, weight: str):
        try:
            result = list(self.database.collection.find({"weight": weight}))
            writeAJson(result, f"pokemons_weight_{weight}")
            return result
        except Exception as e:
            print(e)
            return []

    def get_pokemons_with_avg_spawns_greater_than(self, avg_spawns: float):
        try:
            result = list(self.database.collection.find({"avg_spawns": {"$gt": avg_spawns}}))
            writeAJson(result, f"pokemons_avg_spawns_{avg_spawns}")
            return result
        except Exception as e:
            print(e)
            return []   

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(database=db)

db.resetDatabase()

pokedex.get_all_pokemons()
pokedex.get_pokemon_by_name("Charizard")
pokedex.get_pokemons_by_type("Dragon")
pokedex.get_pokemons_by_weight("10.0 kg")
pokedex.get_pokemons_with_avg_spawns_greater_than(68)