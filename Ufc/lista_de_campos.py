from Ufc.cursos import adicionar_curso, remover_curso, listar_cursos

campos_lista = []

def cadastrar_campus(nome):
    novo_campus = {
        "nome": nome,
        "cursos": []
    }
    campos_lista.append(novo_campus)
    print(f"Campus '{nome}' cadastrado com sucesso!\n")

def procurar_campus(nome):
    for campus in campos_lista:
        if campus["nome"] == nome:
            return campus
    return None

def adicionar_curso_ao_campus(nome_campus, curso):
    campus = procurar_campus(nome_campus)
    if campus:
        adicionar_curso(campus, curso)
    else:
        print(f"Campus '{nome_campus}' não encontrado.\n")

def remover_curso_do_campus(nome_campus, curso):
    campus = procurar_campus(nome_campus)
    if campus:
        remover_curso(campus, curso)
    else:
        print(f"Campus '{nome_campus}' não encontrado.\n")

def consultar_campos():
    if not campos_lista:
        print("Nenhum campus cadastrado.\n")
        return
    print("\n===== LISTA DE CAMPUS E CURSOS =====")
    for campus in campos_lista:
        print(f"Campus: {campus['nome']}")
        listar_cursos(campus)
        print("----------------------------------")
    print()
