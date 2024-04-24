import pygame
import sys
from elevador import Elevador

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
largura = 400
altura = 800

# Defina as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Crie a janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Janela Pygame")

# Crie o elevador
e = Elevador(tela)

# Loop principal do jogo
while True:
    # Lida com eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualize a tela
    tela.fill(PRETO)
    # Desenhe outros elementos na tela aqui
    tela.blit(e.image, e.rect.topleft)
    e.mover(3)

    # Atualize a tela
    pygame.display.flip()

    # Limita a taxa de atualização da tela
    pygame.time.Clock().tick(60)
