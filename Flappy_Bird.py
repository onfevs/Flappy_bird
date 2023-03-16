import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir la pantalla
screen_width = 750
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Definir los colores
white = (255, 255, 255)
black = (0, 0, 0)
blue = (103, 191, 242)
green = (0, 255, 0)

# Definir las fuentes
font_small = pygame.font.Font(None, 32)
font_large = pygame.font.Font(None, 64)

# Definir las variables del juego
gravity = 0.5
bird_speed = 0
pipe_speed = 2
pipe_gap = 100
ground_height = 112
pipe_width = 52
pipe_heights = [200, 250, 300, 350]
score = 0
fps = 60

# Definir las funciones


def draw_pipes():
    pygame.draw.rect(screen, green, top_pipe_rect)
    pygame.draw.rect(screen, green, bottom_pipe_rect)


def show_score():
    score_text = font_small.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))


def reset_game():
    global bird_speed, score, top_pipe_rect, bottom_pipe_rect
    bird_speed = 0
    score = 0
    pipe_height = random.choice(pipe_heights)
    top_pipe_rect = pygame.Rect(
        screen_width, 0, pipe_width, pipe_height - pipe_gap // 2)
    bottom_pipe_rect = pygame.Rect(screen_width, pipe_height + pipe_gap // 2,
                                   pipe_width, screen_height - pipe_height - pipe_gap // 2 - ground_height)


# Crear los rectángulos de los tubos
pipe_height = random.choice(pipe_heights)
top_pipe_rect = pygame.Rect(
    screen_width, 0, pipe_width, pipe_height - pipe_gap // 2)
bottom_pipe_rect = pygame.Rect(screen_width, pipe_height + pipe_gap // 2,
                               pipe_width, screen_height - pipe_height - pipe_gap // 2 - ground_height)

# Crear el rectángulo del pájaro
bird_rect = pygame.Rect(50, 50, 34, 24)

# Crear el rectángulo del suelo
ground_rect_1 = pygame.Rect(
    0, screen_height - ground_height, screen_width, ground_height)
ground_rect_2 = pygame.Rect(
    screen_width, screen_height - ground_height, screen_width, ground_height)

# Definir el reloj
clock = pygame.time.Clock()

# Comenzar el juego
running = True
while running:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -10

    # Mover los tubos hacia la izquierda
    top_pipe_rect.x -= pipe_speed
    bottom_pipe_rect.x -= pipe_speed

    # Si los tubos salen de la pantalla, colocarlos en el otro
    # lado y elegir nuevas alturas
    if top_pipe_rect.right < 0:
        pipe_height = random.choice(pipe_heights)
        top_pipe_rect.left = screen_width
        bottom_pipe_rect.left = screen_width
        top_pipe_rect.height = pipe_height - pipe_gap // 2
        bottom_pipe_rect.top = pipe_height + pipe_gap // 2
        bottom_pipe_rect.height = screen_height - \
            pipe_height - pipe_gap // 2 - ground_height

    # Mover el pájaro
    bird_speed += gravity
    bird_rect.y += bird_speed

    # Si el pájaro toca el suelo o el techo, reiniciar el juego
    if bird_rect.bottom > screen_height - ground_height or bird_rect.top < 0:
        reset_game()

    # Si el pájaro pasa a través del espacio entre los tubos,
    # incrementar la puntuación
    if bird_rect.left > top_pipe_rect.right and not top_pipe_rect.collidepoint(bird_rect.midright):
        score += 1

    # Dibujar los objetos
    screen.fill(blue)
    pygame.draw.rect(screen, black, bird_rect)
    draw_pipes()
    pygame.draw.rect(screen, green, ground_rect_1)
    pygame.draw.rect(screen, green, ground_rect_2)
    show_score()

    # Actualizar la pantalla
    pygame.display.flip()

    # Ajustar la velocidad de fotogramas
    clock.tick(fps)

pygame.quit()
