class Aluno:
    def __init__(self, nome):
        self._nome = nome

    def presenca(self):
        print(f'O aluno {self._nome} está presente.')
        