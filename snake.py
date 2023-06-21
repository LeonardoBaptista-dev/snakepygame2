import pygame
import random

#configuraçoes do jogo
largura = 640
altura = 480
tamanho_bloco = 20
velocidade = 15

#cores 

branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)

pygame.init()

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Snake")
relogio = pygame.time.Clock()

fonte = pygame.font.SysFont(None,25)

def snake(snake_Lista):
    for bloco in snake_Lista:
        pygame.draw.rect(tela,preto,[bloco[0],bloco[1],tamanho_bloco,tamanho_bloco])

def mensagem(msg,cor):
    texto = fonte.render(msg,True,cor)
    tela.blit(texto, [largura/6, altura/2])

def jogo():
    game_over = False
    game_fim = False

    # Posição inicial da cobra

    pos_x = largura/2
    pos_y = altura/2

    # mudança inicial da cobra

    delta_x = 0
    delta_y = 0

    snake_lista = []
    comprimento_snake = 1

    # Posição aleatória da comida

    comida_x = round(random.randrange(0,largura - tamanho_bloco)/20.0)*20.0
    comida_y = round(random.randrange(0,largura - tamanho_bloco)/20.0)*20.0

    while not game_over:
        while game_fim:
            tela.fill(branco)
            mensagem("Fim do Jogo. Precione Cpara Continuar ou Q para Sair.", vermelho)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_fim = False
                if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_q:
                        game_over = True
                        game_fim= False
                    if event.key ==pygame.K_c:
                        jogo()
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -tamanho_bloco
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = tamanho_bloco
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_y = -tamanho_bloco
                    delta_x = 0
                elif event.key == pygame.K_DOWN:
                    delta_y = tamanho_bloco
                    delta_x = 0
        if pos_x >= largura or pos_x <0 or pos_y >= altura or pos_y< 0:
            game_fim = True

        pos_x += delta_x
        pos_y += delta_y
        tela.fill(branco)
        pygame.draw.rect(tela,vermelho, [comida_x,comida_y, tamanho_bloco,tamanho_bloco])        

        snake_cabeca = []
        snake_cabeca.append(pos_x)
        snake_cabeca.append(pos_y)
        snake_lista.append(snake_cabeca)

        if len(snake_lista)> comprimento_snake:
            del snake_lista[0]

        for segmento in snake_lista[:-1]:
            if segmento ==snake_cabeca:
                game_fim = True
        
        snake(snake_lista)
        pygame.display.update()
        if pos_x == comida_x and pos_y == comida_y:
            comida_x = round(random.randrange(0,largura-tamanho_bloco)/20.0)*20.0
            comida_y = round(random.randrange(0,altura-tamanho_bloco)/20.0)*20.0
            comprimento_snake+=1
        
        relogio.tick(velocidade)
    
    pygame.quit()

jogo()
        
                

                







    