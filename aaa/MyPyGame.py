import pygame
import random

# Iniciar Pygame e criar janela
pygame.init()
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pong")

# Cores
FUNDO_COLOR = (0, 0, 0)
BOLA_COLOR = (255, 255, 255)
P1_COLOR = (255, 0, 0)
P2_COLOR = (0, 255, 0)
PONTOS_COLOR = (255, 255, 255)

# Constantes
LARGURA_RAQUETE = 10
ALTURA_RAQUETE = 100
VEL_RAQUETE = 7

RaioBola = 10
Vel_Bola_x = 5
Vel_Bola_y = 5

# ====== Classe Raquete ====== #
class Raquete:
    def __init__(self, x, y, cor):
        self.rect = pygame.Rect(x, y, LARGURA_RAQUETE, ALTURA_RAQUETE)
        self.cor = cor

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, self.rect)

    def mover(self, tecla_cima, tecla_baixo):
        teclas = pygame.key.get_pressed() 
        if teclas[tecla_cima] and self.rect.top > 0:
            self.rect.y -= VEL_RAQUETE
        if teclas[tecla_baixo] and self.rect.bottom < ALTURA_TELA:
            self.rect.y += VEL_RAQUETE
class Bola:
    def __init__(self,x,y):
        self.rect = pygame.Rect(x - RaioBola , y - RaioBola , RaioBola * 2, RaioBola * 2)
        
        #Velocidade\Direção pr x e y
        self.vel_x = Vel_Bola_x * random.choice((1,-1))
        self.vel_y = Vel_Bola_y * random.choice((1,-1))
        
    def desenhar(self, tela):
        pygame.draw.ellipse(tela, BOLA_COLOR, self.rect) 
    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
    def Colisao(self, P1,P2):
        if self.rect.top <= 0 or self.rect.bottom >= ALTURA_TELA:
            self.vel_y *= -1
        if self.rect.colliderect(P1) or self.rect.colliderect(P2):
            self.vel_x *= -1
    
    def Resetar(self):
         self.rect.x = LARGURA_TELA // 2 -RaioBola
         self.rect.y = ALTURA_TELA // 2 -RaioBola 
        
         self.vel_x *= -1
         self.vel_y = Vel_Bola_y * random.choice((1,-1))
        
         pygame.time.delay(500)

# Criar fluxo principal
relogio = pygame.time.Clock()
rodando = True

P1 = Raquete(10, ALTURA_TELA / 2 - ALTURA_RAQUETE / 2, P1_COLOR)
P2 = Raquete(LARGURA_TELA - 20, ALTURA_TELA / 2 - ALTURA_RAQUETE / 2, P2_COLOR)

Minha_Bola = Bola(LARGURA_TELA / 2, ALTURA_TELA / 2)

PontosP1= 0
PontosP2= 0

pontos = 0
fonte = pygame.font.SysFont("bahnschrift", 35)

# ====== Loop Principal ====== #
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
     
    
    
    #====== TURBO ======#
    if PontosP1 + PontosP2 >= 5:
        Vel_Bola_x = 10
        Vel_Bola_y = 10
        VEL_RAQUETE = 12
    # Movendo as raquetes
    P1.mover(pygame.K_w, pygame.K_s)
    P2.mover(pygame.K_UP, pygame.K_DOWN)
    Minha_Bola.mover()

    # Atualizando tela
    tela.fill(FUNDO_COLOR)
    P1.desenhar(tela)
    P2.desenhar(tela)
    Minha_Bola.desenhar(tela)
    
    texto_pontos = fonte.render(f"({PontosP1})X({PontosP2})", True, PONTOS_COLOR)
    tela.blit(texto_pontos, (350,0))

    pygame.display.flip()
    relogio.tick(60)
    #====== Verificar Colizão ======#
    Minha_Bola.Colisao(P1.rect, P2.rect)
    if Minha_Bola.rect.left < 0:
         Minha_Bola.Resetar()
         PontosP2+=1
    if Minha_Bola.rect.right > LARGURA_TELA:
         Minha_Bola.Resetar()
         PontosP1+=1
    
pygame.quit()

