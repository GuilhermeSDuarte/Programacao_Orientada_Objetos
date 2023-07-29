class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("auauauaauauau")

    def parar(self):
        print("A bicicleta parou!")

    def pedalar(self):
        print("Vrummmmmmmmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}'for chave, valor in self.__dict__.items()])}"

bike = Bicicleta("Azul", "Shimano", 2023, 1000)

bike.pedalar()
bike.buzinar()
bike.parar()



bike2 = Bicicleta("Vermelha", "Caloi", 2022, 600)

bike2.pedalar()
bike2.buzinar()
bike2.parar()

print(bike.valor, bike.modelo, bike.cor, bike.ano)
print(bike2.valor, bike2.modelo, bike2.cor, bike2.ano)

print(bike)