import pygame
from datetime import datetime
import math

RES = WIDTH, HEIGHT = 1280, 720
H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2
RADIUS = H_HEIGHT - 50

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))

font = pygame.font.SysFont('Arial', 50)


def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + RADIUS * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + RADIUS * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    surface.fill(pygame.Color("black"))
    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

    pygame.draw.circle(surface, pygame.Color('slategray'), (H_WIDTH, H_HEIGHT), RADIUS)
    pygame.draw.line(surface, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(surface, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    pygame.draw.line(surface, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)

    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('green'), pygame.Color('orange'))
    surface.blit(time_render, (0, 0))

    pygame.display.flip()
    clock.tick(20)
