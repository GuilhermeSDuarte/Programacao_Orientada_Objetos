from abc import ABC, abstractmethod

#A classe se tornou abstrata, não sendo possível ser instanciada, o mesmo para seus metodos.
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

#Como ela tem herança da classe Controle Remoto, é obrigatório que você defina os métodos da classe "pai".
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Tv Ligada")

    def desligar(self):
        print("Tv desligada")

controle = ControleTV()
controle.ligar()
controle.desligar()