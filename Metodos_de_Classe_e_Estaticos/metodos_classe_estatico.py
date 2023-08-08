class Pessoa:

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    #Método de Classe.
    @classmethod
    def criar(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    #Método estático.
    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p = Pessoa("Guilherme", 22)
print(p.nome, p.idade)

p2 = Pessoa.criar(2001, 8, 2, "Gui")
print(p.nome, p.idade)

print(Pessoa.maior_idade(22))