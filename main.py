import pygame
from src.core.settings import WIDTH, HEIGHT, FPS, WHITE
from src.entities.car import Car
from src.entities.enemy_car import EnemyCar
from src.entities.track import Track
from src.core.utils import draw_text
from src.scenes.game_over import game_over_screen

# Inicializa o pygame
pygame.init()

score = 0  

while running:
    clock.tick(FPS)
    screen.fill((50, 50, 50))  

    # Atualiza a pontuação
    score += 1  

    # Desenha a pontuação na tela
    draw_text(screen, f"Pontuação: {score}", 30, WIDTH // 2, 30)


# Cria a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Corrida Pygame")

# Carrega os elementos do jogo
player = Car(WIDTH // 2, HEIGHT - 120)
enemy_cars = [EnemyCar() for _ in range(3)]
track = Track()

# Loop do jogo
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    screen.fill((50, 50, 50))  # Fundo cinza escuro

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    player.move(keys)

    # Atualiza elementos
    track.update()
    for enemy in enemy_cars:
        enemy.update()

    # Desenha elementos
    track.draw(screen)
    player.draw(screen)
    for enemy in enemy_cars:
        enemy.draw(screen)


for enemy in enemy_cars:
    if player.rect.colliderect(enemy.rect):
        action = game_over_screen(screen, score)
        if action == "restart":
            # Reinicia o jogo
            player = Car(WIDTH // 2, HEIGHT - 120)
            enemy_cars = [EnemyCar() for _ in range(3)]
            score = 0

    pygame.display.update()

pygame.quit()
