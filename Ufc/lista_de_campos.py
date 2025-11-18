from Ufc.cursos import Curso

class Campus:
    def __init__(self, nome):
        self.nome = nome
        self.cursos = []

    def adicionar_curso(self, curso_nome):
        novo_curso = Curso(curso_nome)
        if novo_curso in self.cursos:
            print(f"Curso '{curso_nome}' já está cadastrado no campus '{self.nome}'.\n")
            return
        self.cursos.append(novo_curso)
        print(f"Curso '{curso_nome}' adicionado ao campus '{self.nome}' com sucesso!\n")

    def remover_curso(self, curso_nome):
        temp_curso = Curso(curso_nome)
        for curso in self.cursos:
            if curso == temp_curso:
                self.cursos.remove(curso)
                print(f"Curso '{curso_nome}' removido do campus '{self.nome}' com sucesso!\n")
                return
        print(f"O curso '{curso_nome}' não está cadastrado neste campus.\n")

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
        else:
            print("Cursos:")
            for c in self.cursos:
                print(f" - {c.nome}")


campos_lista = []

def cadastrar_campus(nome):
    if procurar_campus(nome):
        print(f"Campus '{nome}' já está cadastrado.\n")
        return
    campus = Campus(nome)
    campos_lista.append(campus)
    print(f"Campus '{nome}' cadastrado com sucesso!\n")


def procurar_campus(nome):
    for campus in campos_lista:
        if campus.nome.lower() == nome.lower():
            return campus
    return None


def consultar_campos():
    if not campos_lista:
        print("Nenhum campus cadastrado.\n")
        return

    print("\n===== LISTA DE CAMPUS E CURSOS =====")
    for campus in campos_lista:
        print(f"Campus: {campus.nome}")
        campus.listar_cursos()
        print("----------------------------------")
    print()
