import pygame
from day_14_AB import Map
from pygame import Surface, Rect
from typing import Tuple

already_drawn: Tuple = set()


def draw_walls(win: Surface, map: Map, ratio: int) -> None:
    for x, y in map.walls:
        pos_x = (x - map.min_x) * ratio
        pos_y = (y - map.min_y) * ratio
        pygame.draw.rect(win, (255, 0, 0), (pos_x, pos_y, ratio, ratio))


def draw_sand(win: Surface, map: Map, ratio: int) -> None:
    global already_drawn
    for x, y in map.occupied:
        if (x, y) not in map.walls and (x, y) not in already_drawn:
            pos_x = (x - map.min_x) * ratio + ratio // 2
            pos_y = (y - map.min_y) * ratio + ratio // 2
            # pygame.draw.rect(win, (0, 250, 0), (pos_x, pos_y, ratio, ratio))
            pygame.draw.circle(win, (0, 250, 0), (pos_x, pos_y), ratio // 2)
            already_drawn.add((x, y))


def clean_rect(win: Surface, rect: Rect) -> None:
    pygame.draw.rect(win, (0, 0, 0), rect)


def draw_current_sand(win: Surface, map: Map, ratio: int) -> Rect:
    x, y = map.current_drop
    pos_x = (x - map.min_x) * ratio + ratio // 2
    pos_y = (y - map.min_y) * ratio + ratio // 2
    return pygame.draw.circle(win, (0, 0, 255), (pos_x, pos_y), ratio // 2)


def draw_score(win: Surface, value: int) -> None:
    font = pygame.font.Font("freesansbold.ttf", 28)
    text = font.render(f"{value}", True, (128, 128, 128), (0, 0, 0))
    text_rect: Rect = text.get_rect()
    text_rect.topleft = (0, 0)
    win.blit(text, text_rect)


def main() -> None:
    global already_drawn
    display_width = 1024
    display_height = 800
    input_filename = f"day_14_input_sample.txt"
    input_filename = f"day_14_input.txt"
    map: Map = Map(input_filename, with_floor=False, debug=False)
    map_width = map.max_x - map.min_x + 1
    map_height = map.max_y - map.min_y + 1
    ratio = min([display_width // map_width, display_height // map_height])

    pygame_icon = pygame.image.load("adventofcode.png")
    pygame.display.set_icon(pygame_icon)

    pygame.init()
    win: Surface = pygame.display.set_mode((map_width * ratio, map_height * ratio))
    pygame.display.set_caption("AoC 2022 - day 14")

    # Indicates pygame is running
    run = True
    continue_drop_sand = True

    # Infinite loop
    number_sand = 0
    previous = None
    win.fill((0, 0, 0))
    draw_walls(win, map, ratio)
    pygame.display.update()
    pygame.time.delay(2000)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_sand(win, map, ratio)
        draw_score(win, number_sand)

        # drawing object on screen which is rectangle here
        if not continue_drop_sand:
            win.fill((0, 0, 0))
            draw_walls(win, map, ratio)
            already_drawn = set()
            draw_sand(win, map, ratio)
            draw_score(win, number_sand - 1)
            pygame.display.update()
            pygame.time.delay(100)
            continue
        number_sand += 1
        previous = None
        for res in map.drop_sand_iter():
            if previous:
                # clean_rect(win, previous)
                pass
            previous = draw_current_sand(win, map, ratio)
            pygame.display.update()
            # pygame.time.delay(5)

        continue_drop_sand = res == True
        # it refreshes the window
        pygame.display.update()
        pygame.time.delay(5)
    pygame.quit()


if __name__ == "__main__":
    main()
