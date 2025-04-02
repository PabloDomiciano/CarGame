import pygame
from src.core.settings import WIDTH, HEIGHT

class Car:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/player_car.png")  # Imagem do carro
        self.image = pygame.transform.scale(self.image, (50, 100))  # Redimensiona a imagem
        self.rect = self.image.get_rect(center=(x, y))  # Define a posição inicial
        self.speed = 5  # Velocidade do carro

    def move(self, keys):
        """Movimenta o carro com as setas do teclado"""
        if keys[pygame.K_LEFT] and self.rect.left > 50:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH - 50:
            self.rect.x += self.speed

    def draw(self, screen):
        """Desenha o carro na tela"""
        screen.blit(self.image, self.rect)
