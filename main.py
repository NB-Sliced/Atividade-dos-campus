from Ufc.lista_de_campos import (
    cadastrar_campus,
    procurar_campus,
    adicionar_curso_ao_campus,
    remover_curso_do_campus,
    consultar_campos
)

def menu():
    while True:
        print("===== MENU UFC =====")
        print("1 - Cadastrar Campus")
        print("2 - Procurar Campus")
        print("3 - Adicionar Curso")
        print("4 - Remover Curso")
        print("5 - Consultar Campus e Cursos")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Nome do novo campus: ")
            cadastrar_campus(nome)

        elif opc == "2":
            nome = input("Nome do campus para procurar: ")
            campus = procurar_campus(nome)
            if campus:
                print(f"Campus encontrado: {campus['nome']}")
            else:
                print("Campus não encontrado.\n")

        elif opc == "3":
            nome = input("Nome do campus: ")
            curso = input("Nome do curso a adicionar: ")
            adicionar_curso_ao_campus(nome, curso)

        elif opc == "4":
            nome = input("Nome do campus: ")
            curso = input("Nome do curso a remover: ")
            remover_curso_do_campus(nome, curso)

        elif opc == "5":
            consultar_campos()

        elif opc == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
