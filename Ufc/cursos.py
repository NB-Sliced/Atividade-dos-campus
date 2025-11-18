def adicionar_curso(campus, curso):
    campus["cursos"].append(curso)
    print(f"Curso '{curso}' adicionado ao campus '{campus['nome']}' com sucesso!\n")

def remover_curso(campus, curso):
    if curso in campus["cursos"]:
        campus["cursos"].remove(curso)
        print(f"Curso '{curso}' removido do campus '{campus['nome']}' com sucesso!\n")
    else:
        print(f"O curso '{curso}' não está cadastrado neste campus.\n")

def listar_cursos(campus):
    if not campus["cursos"]:
        print("Nenhum curso cadastrado.")
    else:
        print("Cursos:")
        for c in campus["cursos"]:
            print(f" - {c}")
