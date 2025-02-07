import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Map settings
MAP_SIZE = 8
TILE_SIZE = 64
WORLD_MAP = [
    "########",
    "#      #",
    "#  ##  #",
    "#  ##  #",
    "#      #",
    "#  ##  #",
    "#      #",
    "########"
]

# Player settings
player_x, player_y = 150, 150  # Starting position
player_angle = 0
FOV = math.pi / 3  # Field of view (60 degrees)
NUM_RAYS = 120
MAX_DEPTH = TILE_SIZE * MAP_SIZE
DELTA_ANGLE = FOV / NUM_RAYS
RAY_STEP = 5
SPEED = 3
ROT_SPEED = 0.05

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


def cast_rays():
    """ Raycasting function to simulate 3D perspective """
    global player_x, player_y, player_angle
    start_angle = player_angle - FOV / 2
    for ray in range(NUM_RAYS):
        angle = start_angle + ray * DELTA_ANGLE
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        for depth in range(0, MAX_DEPTH, RAY_STEP):
            target_x = int(player_x + depth * cos_a)
            target_y = int(player_y + depth * sin_a)

            if WORLD_MAP[target_y // TILE_SIZE][target_x // TILE_SIZE] == "#":
                depth *= math.cos(player_angle - angle)  # Fix fisheye effect
                wall_height = int(HEIGHT / (depth / 10 + 0.01))
                color = (255 - min(255, depth // 5), 255 - min(255, depth // 5), 255)
                pygame.draw.rect(screen, color, (ray * (WIDTH // NUM_RAYS), HEIGHT // 2 - wall_height // 2, WIDTH // NUM_RAYS, wall_height))
                break


def draw_minimap():
    """ Draws a simple minimap """
    map_scale = 8
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            color = WHITE if WORLD_MAP[y][x] == "#" else BLACK
            pygame.draw.rect(screen, color, (x * TILE_SIZE // map_scale, y * TILE_SIZE // map_scale, TILE_SIZE // map_scale, TILE_SIZE // map_scale))

    # Draw player on minimap
    player_minimap_x = player_x // map_scale
    player_minimap_y = player_y // map_scale
    pygame.draw.circle(screen, RED, (int(player_minimap_x), int(player_minimap_y)), 3)


def move_player():
    """ Handles player movement """
    global player_x, player_y, player_angle
    keys = pygame.key.get_pressed()
    new_x, new_y = player_x, player_y

    if keys[pygame.K_w]:  # Move forward
        new_x += SPEED * math.cos(player_angle)
        new_y += SPEED * math.sin(player_angle)
    if keys[pygame.K_s]:  # Move backward
        new_x -= SPEED * math.cos(player_angle)
        new_y -= SPEED * math.sin(player_angle)
    if keys[pygame.K_a]:  # Strafe left
        new_x += SPEED * math.sin(-player_angle)
        new_y += SPEED * math.cos(player_angle)
    if keys[pygame.K_d]:  # Strafe right
        new_x -= SPEED * math.sin(-player_angle)
        new_y -= SPEED * math.cos(player_angle)

    # Collision detection
    if WORLD_MAP[int(new_y // TILE_SIZE)][int(new_x // TILE_SIZE)] == " ":
        player_x, player_y = new_x, new_y

    if keys[pygame.K_LEFT]:  # Rotate left
        player_angle -= ROT_SPEED
    if keys[pygame.K_RIGHT]:  # Rotate right
        player_angle += ROT_SPEED


# Game loop
running = True
while running:
    screen.fill(BLACK)
    cast_rays()
    draw_minimap()
    move_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
