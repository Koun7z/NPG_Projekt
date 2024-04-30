import pygame
import src.Time as Time
Input = []

def main():
    #Input raczej powinien być w module typu GameManager
    global Input

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 18)


    fps = 0

    fpsSum = 0
    fpsSumNum = 0
    fpsTimer = 0

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window

        if(fpsTimer >= 1):
            fps = fpsSum / fpsSumNum
            fpsSum = 0
            fpsSumNum = 0
            fpsTimer = 0
        else:
            fpsTimer += Time.DeltaTime
            fpsSum += 1/Time.DeltaTime
            fpsSumNum += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Input Handling
            if event.type == pygame.KEYDOWN:

                #Check for ctrl pressed, z jakiegoś podowu żaden z enumow nie daje liczby ktorej potrzebuje
                if event.mod == 64 or event.mod == 128:
                    continue

                match event.key:
                    case pygame.K_ESCAPE:
                        Input.clear()

                    case pygame.K_BACKSPACE:
                        if len(Input) > 0:
                            Input.pop()

                    case pygame.K_CAPSLOCK:
                        pass

                    case pygame.K_TAB:
                        pass

                    case pygame.K_LCTRL:
                        pass

                    case pygame.K_RCTRL:
                        pass

                    case pygame.K_LSHIFT:
                        pass

                    case pygame.K_RSHIFT:
                        pass

                    case _:
                        Input.append(event.unicode)

            # That's all for input

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255, 0, 255,))

        # RENDER YOUR GAME HERE
        text_surface = font.render(''.join(Input), True, (0, 0, 0))
        screen.blit(text_surface, ((1280 / 2) - len(Input) * 4.5, 720 / 2))

        text_surface = font.render(f"fps: {fps}", True, (0, 0, 0))
        screen.blit(text_surface, (100, 100))

        # flip() the display to put your work on screen
        pygame.display.flip()

        Time.Update(clock.tick(240) / 1000)  # limits FPS to 240

    pygame.quit()


if __name__ == "__main__":
    main()