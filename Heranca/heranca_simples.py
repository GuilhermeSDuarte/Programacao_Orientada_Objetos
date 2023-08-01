class Veiculos:

    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor!")

class Motocicleta(Veiculos):
    pass

class Carro(Veiculos):
    pass

class Caminhao(Veiculos):

    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}, estou carregado")

moto = Motocicleta("Preta", "abc-123", 2)
print(moto.cor)
moto.ligar_motor()

carro = Carro("Vermelho", "xyz-987", 4)
print(carro.cor)
carro.ligar_motor()

caminhao = Caminhao("Azul", "afsa-asf", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao.cor)