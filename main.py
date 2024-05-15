import pygame
import pygame_gui

CHAR_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ą', 'ę', 'ó', 'ź', 'ż', 'ć', ',', '.', '?', ':', ';', '1', '2',
                 '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-',
                 '_', '+', '=', '`', '~']

target: str
done = False

WIDTH = 1280
HEIGHT = 720


def render_text(text: str, font: pygame.font.Font) -> pygame.Surface:
    global done
    global target

    i = 0
    for char in text:
        if char == target[i]:
            i += 1
        else:
            break

    if i == len(target) - 1:
        done = True

    good_text = text[0:i]
    bad_text = text[i:]

    good_size = font.size(good_text)
    bad_size = font.size(bad_text)

    target_render = font.render(target, True, (69, 70, 76))
    input_render = font.render(good_text, True, (230, 181, 37))

    font.set_underline(True)
    line_render = font.render(" ", True, (230, 181, 37))
    input_render_err = font.render(bad_text, True, (205, 115, 85))
    font.set_underline(False)

    rect = pygame.Rect(good_size[0], 0, bad_size[0], bad_size[1])
    pygame.draw.rect(target_render, (89, 96, 128,), rect,)

    target_render.blit(input_render, (0, 0))
    target_render.blit(line_render, (good_size[0], 0))
    target_render.blit(input_render_err, (good_size[0], 0))

    return target_render


def main():
    global target
    global CHAR_LIST
    global done
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    pygame.font.init()
    font = pygame.font.SysFont("Consolas", 35)
    font.align = pygame.FONT_LEFT

    input = []
    deltaTime = 0.017

    file = open('lorem.txt', 'r')
    lines = file.readlines()
    n = 0
    target = lines[n]
    file.close()

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_BACKSPACE:
                if len(input) > 0:
                    input.pop()
                continue

            if event.key == pygame.K_ESCAPE:
                input.clear()
                continue

            if event.key == pygame.K_SPACE:
                input.append(" ")
                continue

            for char in event.unicode:
                if char.lower() in CHAR_LIST:
                    input.append(char)

        if done:
            n += 1
            target = lines[n]
            input.clear()

            done = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((89, 96, 128,))

        size = font.size(target)

        screen.blit(render_text("".join(input), font), ((WIDTH - size[0])/2, HEIGHT/2))

        text_surface = font.render(f"fps: {clock.get_fps()}" , True, (0, 0, 0))
        screen.blit(text_surface, (100, 100))

        # flip() the display to put your work on screen
        pygame.display.flip()

        deltaTime = clock.tick(120) / 1000  # limits FPS to 60

    pygame.quit()






if __name__ == "__main__":
    main()