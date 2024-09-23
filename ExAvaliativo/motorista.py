class Motorista:

    def __init__(self, nota):
        self.nota = nota
        self.corridas = []

    def adicionar_corrida(self, corrida):
        self.corridas.append(corrida)

    def to_dict(self):
        return {
            "nota": self.nota,
            "corridas": [corrida.to_dict() for corrida in self.corridas]
        }