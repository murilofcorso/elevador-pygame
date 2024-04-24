import pygame

class Elevador(pygame.sprite.Sprite):
    def __init__(self, tela):
        super().__init__()
        self.tela = tela
        self.largura = 70
        self.altura = 130
        self.image = pygame.surface.Surface((self.largura, self.altura), pygame.SRCALPHA)
        self.image.fill("WHITE")
        self.rect = self.image.get_rect()

        self.status = "parado"
        self.andares = {
            self.tela.get_height() - (0 * self.altura): 0,
            self.tela.get_height() - (1 * self.altura): 1,
            self.tela.get_height() - (2 * self.altura): 2,
            self.tela.get_height() - (3 * self.altura): 3 
        }
        self.andar_atual = 0
        self.rect.bottomleft = (self.tela.get_width()/2 - self.largura/2, self.tela.get_height() - (self.andar_atual * self.altura))
        self.chamados = []

    def mover(self, destino):
        if self.status == "parado":
            self.status = "movendo" 

        if self.rect.bottom > self.tela.get_height() - (destino * self.altura):
            self.rect.y -= 2
        elif self.rect.bottom < self.tela.get_height() - (destino * self.altura):
            self.rect.y += 2
        else:
            self.status = "parado"

        if self.rect.bottom in self.andares.keys():
            self.andar_atual = self.andares[self.rect.bottom]
                
            
    def abrir_porta(self):
        if self.status == "parado":
            self.status = "porta_aberta"


    def fechar_porta(self):
        if self.status == "porta_aberta":
            self.status = "parado"


    def adicionar_chamado(self, andar):
        if andar not in self.chamados:
            self.chamados.append(andar)
    
    
    def retornar_proximo_chamado(self):
        if len(self.chamados) > 0:
            if self.andar_atual != self.chamados[0]:
                return self.chamados[0]
            else:
                self.chamados.pop(0)
                return self.andar_atual
        else:
            return self.andar_atual


    def update(self):
        self.mover(self.retornar_proximo_chamado())
        print(self.chamados)
