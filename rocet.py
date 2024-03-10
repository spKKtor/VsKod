import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Встановлення вікна гри
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Літаюча ракета")

# Колір фону і ракети
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Розміри ракети та перешкод
rocket_width, rocket_height = 50, 50
obstacle_width, obstacle_height = 50, 200

# Параметри швидкості та гравця
player_x, player_y = 50, HEIGHT // 2 - rocket_height // 2
speed = 5
score = 0

# Створення списків перешкод та їх початкових координат
obstacles = []
obstacle_x = WIDTH + 50
obstacle_gap = 150
obstacle_speed = 5

clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsans', 30)

def redraw_window():
    win.fill(WHITE)
    pygame.draw.rect(win, RED, (player_x, player_y, rocket_width, rocket_height))

    for obstacle in obstacles:
        pygame.draw.rect(win, RED, obstacle)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(score_text, (10, 10))

    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_s] and player_y < HEIGHT - rocket_height:
        player_y += speed

    # Додавання перешкод та оновлення їх руху
    if len(obstacles) == 0 or obstacles[-1][0] < WIDTH - obstacle_gap:
        obstacle_height = random.randint(100, 300)
        obstacles.append(pygame.Rect(obstacle_x, 0, obstacle_width, obstacle_height))
        obstacles.append(pygame.Rect(obstacle_x, obstacle_height + obstacle_gap, obstacle_width, HEIGHT - obstacle_height - obstacle_gap))

    # Переміщення та видалення перешкод
    for obstacle in obstacles[:]:
        obstacle.x -= obstacle_speed
        if obstacle.x + obstacle.width < 0:
            obstacles.remove(obstacle)
            score += 1

    # Перевірка на зіткнення
    for obstacle in obstacles:
        if obstacle.colliderect(pygame.Rect(player_x, player_y, rocket_width, rocket_height)):
            pygame.quit()

    redraw_window()

pygame.quit()
