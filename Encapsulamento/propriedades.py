class Pessoa:

    def __init__(self, nome, ano_nacimento):
        self._nome = nome
        self._ano_nascimento = ano_nacimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2023
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Guilherme", 2001)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

class Foo:

    def __init__(self, x=None):
        self._x = x

    @property
    #Serve para transformar o método em uma propriedade
    def x(self):
        return self._x or 0

    @x.setter
    #Serve para permitir que você incremente um valor ou altere na propriedade
    def x(self, value):
        self._x += value

    @x.deleter
    #Serve para deletar a propriedade, mas nem sem há a necessidade de deletar o metodo, podemos zerar.
    def x(self):
        self._x = 0
        #del self._x

foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)