import pygame
import pygame_widgets
from pygame_widgets.button import Button

from board import Board

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    board = Board(20, 20)
    board.set_view(100, 100, 20)
    running = True
    update_board = [False, False]
    font = pygame.font.SysFont('Bahnschrift SemiBold', 25)
    button = Button(
        screen, 600, 100, 70, 35, text='Hello', fontSize=25, textColour='green',
        font=font,
        inactiveColour=(43, 43, 43),
        hoverColour=(50, 50, 50),
        pressedColour=(100, 100, 100),
        onClick=board.reset
    )
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)
                if event.button == 4:
                    update_board[1] = True
        screen.fill((43, 43, 43))
        if any(update_board):
            board.update()
            update_board[1] = False
        board.render(screen)
        pygame_widgets.update(events)
        button.draw()
        pygame.display.flip()
    pygame.quit()
