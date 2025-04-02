import pygame
from src.core.settings import WIDTH, HEIGHT, GAME_SPEED, WHITE

class Track:
    def __init__(self):
        self.line_width = 10
        self.line_height = 40
        self.gap = 20
        self.lines = [pygame.Rect(WIDTH//2 - 5, i, self.line_width, self.line_height) for i in range(0, HEIGHT, self.line_height + self.gap)]

    def update(self):
        """Move as linhas para baixo e reposiciona quando saem da tela"""
        for line in self.lines:
            line.y += GAME_SPEED
            if line.y > HEIGHT:
                line.y = -self.line_height

    def draw(self, screen):
        """Desenha as linhas da pista"""
        for line in self.lines:
            pygame.draw.rect(screen, WHITE, line)
