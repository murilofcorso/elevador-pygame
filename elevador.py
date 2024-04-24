import time
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

        print(self.status)
                
            
    def abrir_porta(self):
        if self.status == "parado":
            self.status = "porta_aberta"


    def fechar_porta(self):
        if self.status == "porta_aberta":
            self.status = "parado"


    def adicionar_chamado(self, andar, direcao):
        if (andar, direcao) not in self.chamados:
            self.chamados.append((andar, direcao))

        
