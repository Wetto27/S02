class Professor:
    def __init__(self, nome):
        self._nome = nome

    def ministrar_aula(self, assunto):
        print(f'O professor {self._nome} está ministrando uma aula sobre {assunto}.')
        