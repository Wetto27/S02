from motoristaDAO import MotoristaDAO
from corrida import Corrida
from motorista import Motorista
from passageiro import Passageiro
from bson import ObjectId

class MotoristaCLI:
    def __init__(self, motorista_dao):
        self.motorista_dao = motorista_dao

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Criar Motorista")
            print("2. Pesquisar Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            op = int(input("Digite uma opção: "))
            
            if op == 1:
                self.create_motorista()
            elif op == 2:
                self.read_motorista()
            elif op == 3:
                self.update_motorista()
            elif op == 4:
                self.delete_motorista()
            elif op == 5:
                print("Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def create_motorista(self):
        nota = int(input("Nota do Motorista: "))
        motorista = Motorista(nota)
        
        while True:
            nome = input("Nome do Passageiro: ")
            documento = input("Documento do Passageiro: ")
            passageiro = Passageiro(nome, documento)
            nota_corrida = int(input("Nota da Corrida: "))
            distancia = float(input("Distância da Corrida: "))
            valor = float(input("Valor da Corrida: "))
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            motorista.adicionar_corrida(corrida)
            adicionar_corrida = input("Adicionar mais corridas? (sim/não): ")
            if adicionar_corrida.lower() != 'sim':
                break
        
        motorista_id = self.motorista_dao.create_motorista(motorista)
        print(f"Motorista criado com sucesso! ID: {motorista_id}")

    def read_motorista(self):
        motorista_id = ObjectId(input("ID do Motorista: "))
        motorista = self.motorista_dao.read_motorista(motorista_id)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        motorista_id = ObjectId(input("ID do Motorista: "))
        nova_nota = int(input("Digite a nova nota: "))
        self.motorista_dao.update_motorista(motorista_id, {"nota": nova_nota})
        print("Nota do motorista atualizada com sucesso!")

    def delete_motorista(self):
        motorista_id = ObjectId(input("ID do Motorista: "))
        self.motorista_dao.delete_motorista(motorista_id)
        print("Motorista deletado com sucesso!")