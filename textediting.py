from pygame import *
from pygame.locals import *

def EditText (screen, background, x, y):
    text = ''
    RED = (255, 0, 0)

    f = font.SysFont(None, 48)
    img = f.render(text, True, RED)

    rect = img.get_rect()
    rect.topleft = (x, y)
    cursor = Rect(rect.topright, (3, rect.height))

    running = True

    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                elif e.key == 13:
                    running = False
                else:
                    if e.key >= 48 and e.key <= 57 or e.key >= 256 and e.key <= 265:
                        text += e.unicode

                img = f.render(text, True, RED)
                rect.size = img.get_size()
                cursor.topleft = rect.topright

        screen.blit(background, (0, 0))  # установить задний фон
        screen.blit(img, rect)

        draw.rect(screen, RED, cursor)
        display.update()

    return text
