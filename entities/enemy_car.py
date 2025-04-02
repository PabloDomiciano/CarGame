import pygame
import random
from src.core.settings import WIDTH, HEIGHT, GAME_SPEED

class EnemyCar:
    def __init__(self):
        self.image = pygame.image.load("assets/images/enemy_car.png")  # Imagem do carro inimigo
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect(center=(random.randint(100, WIDTH - 100), -100))  # Posição inicial
        self.speed = random.randint(GAME_SPEED, GAME_SPEED + 3)  # Velocidade aleatória

    def update(self):
        """Move o carro para baixo"""
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = -100  # Reseta a posição do carro
            self.rect.x = random.randint(100, WIDTH - 100)  # Nova posição aleatória

    def draw(self, screen):
        """Desenha o carro na tela"""
        screen.blit(self.image, self.rect)
