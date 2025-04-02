import pygame
from src.core.settings import WHITE

def draw_text(screen, text, size, x, y):
    """Desenha texto na tela"""
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)
