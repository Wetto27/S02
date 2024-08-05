from models.aluno import Aluno

class Aula:
    def __init__(self, professor, assunto):
        self._professor = professor
        self._assunto = assunto
        self._alunos = []

    def adicionar_aluno(self, aluno):
        self._alunos.append(aluno)

    def listar_presenca(self):
        print(f'Presença na aula sobre {self._assunto}, ministrada pelo professor {self._professor._nome}:')
        for aluno in self._alunos:
            Aluno.presenca(aluno)

        