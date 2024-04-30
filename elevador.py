import pygame

class Elevador(pygame.sprite.Sprite):
    def __init__(self, tela):
        super().__init__()
        self.tela = tela
        self.largura = 70
        self.altura = 130
        self.image = pygame.surface.Surface((self.largura, self.altura), pygame.SRCALPHA)
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

        self.fechou = False
        self.abriu = False


    def mover(self, destino):
        if self.status == "parado":
            self.status = "movendo" 

        if self.status == "movendo":
            if self.rect.bottom > self.tela.get_height() - (destino * self.altura):
                self.rect.y -= 2
            elif self.rect.bottom < self.tela.get_height() - (destino * self.altura):
                self.rect.y += 2
            else:
                self.status = "parado"
                if len(self.chamados) > 0:
                    self.abrir_porta()

        if self.rect.bottom in self.andares.keys():
            self.andar_atual = self.andares[self.rect.bottom]
                
            
    def abrir_porta(self):
        if self.status == "parado":
            self.status = "porta_abrindo"


    def desenhar(self):
        self.image.fill("black")
        if self.status in ("parado", "movendo"):
            self.largura_porta = self.largura/2
            self.pos_porta_direita = self.largura_porta
        else:
            if self.status == "porta_abrindo":
                self.largura_porta -= 1
                self.pos_porta_direita += 1
                if self.largura_porta < -1:
                    self.status = "porta_aberta"
                    self.abriu = True
                    self.abertura_tick = pygame.time.get_ticks()
                    self.fechar_porta()
            elif self.status == "porta_fechando":
                self.largura_porta += 1
                self.pos_porta_direita -= 1
                if self.largura_porta >= self.largura/2:
                    self.status = "porta_fechada"
                    self.fechou = True
                    self.fechamento_tick = pygame.time.get_ticks()
                    self.chamados.pop(0)

        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, self.largura_porta, self.altura))
        pygame.draw.rect(self.image, (255, 255, 255), (self.pos_porta_direita, 0, self.largura_porta, self.altura))


    def fechar_porta(self):
        if self.status == "porta_abrindo":
            self.status = "porta_fechando"


    def cooldowns(self):
        self.tick_atual = pygame.time.get_ticks()
        # cooldown 
        if self.fechou:
            if self.tick_atual - self.fechamento_tick > 1200:
                self.fechou = False
                self.status = "parado"

        if self.abriu:
            if self.tick_atual - self.abertura_tick > 1200:
                self.abriu = False
                self.status = "porta_fechando"


    def adicionar_chamado(self, andar):
        if andar not in self.chamados:
            self.chamados.append(andar)
    
    
    def retornar_proximo_chamado(self):
        if len(self.chamados) > 0:
            if self.andar_atual != self.chamados[0]:
                return self.chamados[0]
            else:
                return self.andar_atual
        else:
            return 0


    def update(self):
        self.cooldowns()
        self.desenhar()
        self.mover(self.retornar_proximo_chamado())
