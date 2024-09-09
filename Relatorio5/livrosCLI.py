from pymongo import MongoClient

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Digite um comando: ")
            if command == "exit":
                print("Até logo!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class LivrosCLI(SimpleCLI):
    def __init__(self):
        super().__init__()
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["relatorio_5"]
        self.collection = self.db["Livros"]
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        _id = input("Digite o ID do livro: ")
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano do livro: "))
        preco = float(input("Digite o preço do livro: "))
        livro = {
            "_id": _id,
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "preco": preco
        }
        self.collection.insert_one(livro)
        print("Livro criado com sucesso!")

    def read_book(self):
        _id = input("Digite o ID do livro: ")
        livro = self.collection.find_one({"_id": _id})
        if livro:
            print(f"Título: {livro['titulo']}")
            print(f"Autor: {livro['autor']}")
            print(f"Ano: {livro['ano']}")
            print(f"Preço: {livro['preco']}")
        else:
            print("Livro não encontrado.")

    def update_book(self):
        _id = input("Digite o ID do livro: ")
        titulo = input("Digite o novo título do livro: ")
        autor = input("Digite o novo autor do livro: ")
        ano = int(input("Digite o novo ano do livro: "))
        preco = float(input("Digite o novo preço do livro: "))
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "preco": preco
        }
        self.collection.update_one({"_id": _id}, {"$set": livro})
        print("Livro atualizado com sucesso!")

    def delete_book(self):
        _id = input("Digite o ID do livro: ")
        self.collection.delete_one({"_id": _id})
        print("Livro deletado com sucesso!")

    def run(self):
        print("Bem-vindo ao menu de livros!")
        print("Comandos: create, read, update, delete, exit")
        super().run()        