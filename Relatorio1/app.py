from models.professor import Professor
from models.aluno import Aluno
from models.aula import Aula

def main():
    professor = Professor("Lucas")
    aluno1 = Aluno("Maria")
    aluno2 = Aluno("Pedro")
    aula = Aula(professor, "Programação Orientada a Objetos")
    aula.adicionar_aluno(aluno1)
    aula.adicionar_aluno(aluno2)
    aula.listar_presenca()

if __name__ == '__main__':
    main()