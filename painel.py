import pygame
from chamador import Chamador


class Painel(pygame.sprite.Sprite):
    def __init__(self, tela, elevador, andares):        
        self.tela = tela
        self.elevador = elevador
        self.andares = andares

        self.largura = 140
        self.altura = 180

        self.image = pygame.surface.Surface((self.largura, self.altura), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topright = (self.tela.get_width() - 30, 30)

        
    def desenhar(self):
        self.image.fill((255, 60, 60))
            
        
    def update(self, evento):
        self.evento = evento
        self.desenhar()