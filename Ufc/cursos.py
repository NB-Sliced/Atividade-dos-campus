class Curso:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __eq__(self, other):
        if isinstance(other, Curso):
            return self.nome.lower() == other.nome.lower()
        return False
