import pygame
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
HALF_HEIGHT = HEIGHT // 2
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
SPEED = 3
ROT_SPEED = 0.05

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def cast_rays():
    """ Raycasting using DDA for optimized performance """
    global player_x, player_y, player_angle
    start_angle = player_angle - FOV / 2

    for ray in range(NUM_RAYS):
        angle = start_angle + ray * DELTA_ANGLE
        sin_a, cos_a = math.sin(angle), math.cos(angle)

        # Step sizes for DDA
        x_step = TILE_SIZE / abs(cos_a) if cos_a != 0 else MAX_DEPTH
        y_step = TILE_SIZE / abs(sin_a) if sin_a != 0 else MAX_DEPTH

        # Initial grid crossings
        x_hit, y_hit = None, None
        depth = 0

        # Checking vertical and horizontal intersections
        for vert in range(2):
            if vert:
                # Vertical checking
                x = ((player_x // TILE_SIZE) + (1 if cos_a > 0 else 0)) * TILE_SIZE
                dx = TILE_SIZE if cos_a > 0 else -TILE_SIZE
                depth = (x - player_x) / cos_a if cos_a else MAX_DEPTH
                y = player_y + depth * sin_a
            else:
                # Horizontal checking
                y = ((player_y // TILE_SIZE) + (1 if sin_a > 0 else 0)) * TILE_SIZE
                dy = TILE_SIZE if sin_a > 0 else -TILE_SIZE
                depth = (y - player_y) / sin_a if sin_a else MAX_DEPTH
                x = player_x + depth * cos_a

            while depth < MAX_DEPTH:
                map_x, map_y = int(x // TILE_SIZE), int(y // TILE_SIZE)

                # ✅ Fix: Prevent out-of-bounds errors
                if 0 <= map_x < MAP_SIZE and 0 <= map_y < MAP_SIZE:
                    if WORLD_MAP[map_y][map_x] == "#":
                        x_hit, y_hit = x, y
                        break
                else:
                    break  # Stop checking if out of bounds

                x += dx if vert else x_step * cos_a
                y += dy if not vert else y_step * sin_a
                depth += x_step if vert else y_step

        # Fix fisheye distortion
        depth *= math.cos(player_angle - angle)

        # Wall height and shading
        wall_height = int(HEIGHT / (depth / 10 + 0.01))
        color_intensity = max(50, 255 - int(depth / 5))  # Darker further away
        wall_color = (color_intensity, color_intensity // 2, color_intensity // 3)

        # Draw wall slice
        pygame.draw.rect(screen, wall_color, (ray * (WIDTH // NUM_RAYS), HALF_HEIGHT - wall_height // 2, WIDTH // NUM_RAYS, wall_height))

        # Draw floor and ceiling shading
        floor_shade = (color_intensity // 2, color_intensity // 3, color_intensity // 4)
        pygame.draw.rect(screen, floor_shade, (ray * (WIDTH // NUM_RAYS), HALF_HEIGHT + wall_height // 2, WIDTH // NUM_RAYS, HEIGHT))
        pygame.draw.rect(screen, (color_intensity // 1.5, color_intensity // 2, color_intensity // 2), (ray * (WIDTH // NUM_RAYS), 0, WIDTH // NUM_RAYS, HALF_HEIGHT - wall_height // 2))


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

    # ✅ Fix: Prevent player from walking through walls
    if 0 <= new_x < TILE_SIZE * MAP_SIZE and 0 <= new_y < TILE_SIZE * MAP_SIZE:
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
