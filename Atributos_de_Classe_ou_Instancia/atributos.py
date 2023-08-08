class Estudante:
#Variavel de classe.
    escola = "DIO"

#Variaveis de instancia.
    def __init__(self,nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_estudante(*objs):
    for obj in objs:
        print(obj)

estudante_1 = Estudante("Guilherme", 1)
estudante_2 = Estudante("Miguel", 2)
mostrar_estudante(estudante_1)
mostrar_estudante(estudante_2)
estudante_2.matricula = 3
Estudante.escola = "Alura"
#Tentar alterar uma variavel de instancia não funciona por meio da classe, o teste abaixo é um exemplo.
Estudante.nome = "Fulaninho"
mostrar_estudante(estudante_1)
mostrar_estudante(estudante_2)