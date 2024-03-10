import pygame
import random

# Ініціалізація Pygame
pygame.init()

# Встановлення вікна гри
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Уникни перешкод")

# Колір фону і ракети
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Розміри ракети та перешкод
rocket_width, rocket_height = 50, 50
obstacle_width, obstacle_height = 50, 50

# Параметри швидкості та гравця
player_x, player_y = 50, HEIGHT // 2 - rocket_height // 2
speed = 7
score = 0

# Створення списків перешкод та їх початкових координат
obstacles = []
obstacle_speed = 7
obstacle_freq = 40
obstacle_counter = 0

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
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_s] and player_y < HEIGHT - rocket_height:
        player_y += speed

    # Додавання нових перешкод
    obstacle_counter += 1
    if obstacle_counter == obstacle_freq:
        obstacle_y = random.randint(0, HEIGHT - obstacle_height)
        obstacles.append(pygame.Rect(WIDTH, obstacle_y, obstacle_width, obstacle_height))
        obstacle_counter = 0

    # Рух перешкод
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed

        # Перевірка на зіткнення з перешкодою
        if obstacle.colliderect(pygame.Rect(player_x, player_y, rocket_width, rocket_height)):
            pygame.quit()

        # Видалення перешкод, які вийшли за межі екрану
        if obstacle.x + obstacle.width < 0:
            obstacles.remove(obstacle)
            score += 1

    redraw_window()

pygame.quit()
