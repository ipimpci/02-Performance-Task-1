import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Unclash Game')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
FPS = 60

square_size = 50
square_x = WIDTH // 2
square_y = HEIGHT - square_size - 10
square_speed = 5

circle_radius = 20
circle_speed = 5
circles = []

def reset_game():
    global square_x, square_y, square_speed, circles, start_time, game_over
    square_x = WIDTH // 2
    square_y = HEIGHT - square_size - 10
    circles = []
    start_time = time.time()
    game_over = False

reset_game()

start_time = time.time()

font = pygame.font.Font(None, 36)

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and game_over:
        reset_game()

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            square_x -= square_speed
        if keys[pygame.K_RIGHT]:
            square_x += square_speed
        if keys[pygame.K_UP]:
            square_y -= square_speed
        if keys[pygame.K_DOWN]:
            square_y += square_speed

        square_x = max(0, min(square_x, WIDTH - square_size))
        square_y = max(0, min(square_y, HEIGHT - square_size))

        if random.randint(1, 20) == 1:
            circle_x = random.randint(circle_radius, WIDTH - circle_radius)
            circle_y = -circle_radius
            circles.append([circle_x, circle_y])

        for circle in circles:
            circle[1] += circle_speed

        circles = [circle for circle in circles if circle[1] < HEIGHT + circle_radius]

        for circle in circles:
            if (square_x < circle[0] < square_x + square_size or
                square_x < circle[0] + circle_radius * 2 < square_x + square_size) and \
               (square_y < circle[1] < square_y + square_size or
                square_y < circle[1] + circle_radius * 2 < square_y + square_size):
                game_over = True
                print("Game Over!")

        elapsed_time = int(time.time() - start_time)

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (square_x, square_y, square_size, square_size))
    for circle in circles:
        pygame.draw.circle(screen, RED, (circle[0], circle[1]), circle_radius)

    time_text = font.render(f"Time: {elapsed_time} seconds", True, WHITE)
    screen.blit(time_text, (10, 10))

    if game_over:
        game_over_text = font.render("GAME OVER!", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

        restart_text = font.render("Press SPACE to Restart", True, WHITE)
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
