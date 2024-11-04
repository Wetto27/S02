from teacher_crud import TeacherCRUD

class CLI:
    def __init__(self):
        self.teacher_crud = TeacherCRUD()

    def run(self):
        while True:
            print("\n1. Create Teacher")
            print("2. Read Teacher")
            print("3. Update CPF")
            print("4. Delete Teacher")
            print("5. Sair")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                name = input("Nome: ")
                ano_nasc = int(input("Ano de Nascimento: "))
                cpf = input("CPF: ")
                self.teacher_crud.create(name, ano_nasc, cpf)
                print("Teacher criado com sucesso!")

            elif choice == "2":
                name = input("Nome do Teacher: ")
                result = self.teacher_crud.read(name)
                print(result)

            elif choice == "3":
                name = input("Nome do Teacher: ")
                newCpf = input("Novo CPF: ")
                self.teacher_crud.update(name, newCpf)
                print("CPF atualizado com sucesso!")

            elif choice == "4":
                name = input("Nome do Teacher: ")
                self.teacher_crud.delete(name)
                print("Teacher deletado com sucesso!")

            elif choice == "5":
                self.teacher_crud.close()
                break

            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    cli = CLI()
    cli.run()