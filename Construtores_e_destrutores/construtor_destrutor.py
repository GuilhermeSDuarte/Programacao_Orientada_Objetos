class Cachorro:

    #Construtor, código para instanciar os objetos dentro da classe.
    def __init__(self, nome, cor, acordado=True):
        print("Instancia iniciada!")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    #Destrutor tem a função de finalizar a instancia, ele serve para finalize o processo alocado na memória quando não utilizado.
    def __del__(self):
        print("Removendo a instancia da classe!")

    def latir(self):
        print("Au Au Au")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco", False)
    print(c.nome)

    c.latir()

    print(c.nome)
    print(c.nome)
    print(c.nome)
    del c
    #print(c.nome)
    #print(c.nome)
    #print(c.nome)

criar_cachorro()