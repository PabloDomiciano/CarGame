import pygame
from src.core.settings import WIDTH, HEIGHT, WHITE
from src.core.utils import draw_text

def game_over_screen(screen, score):
    """Exibe a tela de Game Over"""
    screen.fill((0, 0, 0))  # Tela preta
    draw_text(screen, "GAME OVER", 50, WIDTH // 2, HEIGHT // 3)
    draw_text(screen, f"Pontuação Final: {score}", 30, WIDTH // 2, HEIGHT // 2)
    draw_text(screen, "Pressione R para Reiniciar ou Q para Sair", 20, WIDTH // 2, HEIGHT // 1.5)
    
    pygame.display.update()
    
    # Espera entrada do usuário
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                if event.key == pygame.K_q:
                    pygame.quit()
                    exit()
