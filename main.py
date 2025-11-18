from Ufc.lista_de_campos import (
    cadastrar_campus,
    procurar_campus,
    consultar_campos
)

def adicionar_curso_ao_campus(nome_campus, nome_curso):
    campus = procurar_campus(nome_campus)
    if campus:
        campus.adicionar_curso(nome_curso)
    else:
        print(f"Campus '{nome_campus}' não encontrado.\n")

def remover_curso_do_campus(nome_campus, nome_curso):
    campus = procurar_campus(nome_campus)
    if campus:
        campus.remover_curso(nome_curso)
    else:
        print(f"Campus '{nome_campus}' não encontrado.\n")


def menu():
    while True:
        print("""
===== MENU PRINCIPAL =====
1- Cadastrar Campus
2- Adicionar Curso a um Campus
3- Remover Curso de um Campus
4- Consultar todos os Campus e Cursos
5- Sair
==========================
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do novo campus: ")
            cadastrar_campus(nome)

        elif opcao == "2":
            nome_campus = input("Nome do campus: ")
            nome_curso = input("Nome do curso a adicionar: ")
            adicionar_curso_ao_campus(nome_campus, nome_curso)

        elif opcao == "3":
            nome_campus = input("Nome do campus: ")
            nome_curso = input("Nome do curso a remover: ")
            remover_curso_do_campus(nome_campus, nome_curso)

        elif opcao == "4":
            consultar_campos()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()
