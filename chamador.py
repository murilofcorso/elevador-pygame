class Chamador:
    def __init__(self, elevador, andar):
        self.elevador = elevador
        self.andar = andar
        

    def enviar_chamado(self):
        self.elevador.adicionar_chamado(self.andar)

    