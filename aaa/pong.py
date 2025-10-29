import pygame
import random

#iniciar Pygame e janela
pygame.init()
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong!")

Fundo_Color = (0,0,0)
Bola_Color = (255,255,255)
P1_Color =  (255,0,0)
P2_Color =  (0,255,0)


#======Constantes======#
Largura_Raquetes = 10
Altura_Raquete = 100
Vel_Raquete = 15
#======Classes======#
class Raquete:
    def __init__(self,x,y,cor):
        self.rect = pygame.Rect(x,y,Largura_Raquetes, Altura_Raquete)
        self.cor = cor
    
    def desenhar(self, tela):
        pygame.draw.rect(tela,self.cor, self.rect)
    
    def mover(self, tecla_cima, tecla_baixo):
        teclas = pygame.key.get_pressed()
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -= Vel_Raquete
        if teclas[tecla_baixo] and self.rect.top < ALTURA_TELA:
            self.rect.y += Vel_Raquete
            
#Criar fluxo
relogio = pygame.time.Clock()
Rodando = True

P1 = Raquete(10, ALTURA_TELA / 2 - Altura_Raquete / 2,  P1_Color)
P2 = Raquete(LARGURA_TELA - 20, ALTURA_TELA / 2 - Altura_Raquete / 2,  P2_Color)


while Rodando:
    #======Verficação de Eventos======#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Rodando = False
   
    
    #====== Taxa de Atualização ======#
    tela.fill(Fundo_Color)
    P1.desenhar(tela)
    P2.desenhar(tela)
    pygame.display.flip()
    relogio.tick(60)
    
    #====== Movendo Raquete P1 ======#
    P1.mover(pygame.K_w, pygame.K_s)
    P2.mover(pygame.K_UP, pygame.K_DOWN)
    
    
pygame.quit()