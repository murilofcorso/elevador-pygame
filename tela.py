import pygame
import sys
from elevador import Elevador
from chamador import Chamador

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

# Crie o chamador
c0 = Chamador(e, 0)
c1 = Chamador(e, 1)
c2 = Chamador(e, 2)
c3 = Chamador(e, 3)


# Loop principal do jogo
c3.enviar_chamado()
c2.enviar_chamado()
while True:
    # Lida com eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualize a tela
    tela.fill((80, 80, 255))
    # Desenhe outros elementos na tela aqui
    tela.blit(e.image, e.rect.topleft)
    e.update()

    # Atualize a tela
    pygame.display.flip()

    # Limita a taxa de atualização da tela
    pygame.time.Clock().tick(60)
