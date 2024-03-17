import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from board import Board


def main():
    fps = 20
    pygame.init()
    clock = pygame.time.Clock()
    size = 800, 550
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Life')

    board = Board(20, 20)
    board.set_view(20, 20, 20)
    running = True
    update_board = False
    font = pygame.font.SysFont('Bahnschrift SemiBold', 25)
    reset_button = Button(screen, 600, 100, 70, 35, text='Reset', fontSize=25, textColour='green', font=font,
                          inactiveColour=(43, 43, 43), hoverColour=(50, 50, 50), pressedColour=(100, 100, 100),
                          onClick=board.reset)
    start_button = Button(screen, 600, 50, 70, 35, text='Start', fontSize=25, textColour='green', font=font,
                          inactiveColour=(43, 43, 43), hoverColour=(50, 50, 50), pressedColour=(100, 100, 100),
                          onClick=board.start)
    stop_button = Button(screen, 700, 50, 70, 35, text='Stop', fontSize=25, textColour='green', font=font,
                         inactiveColour=(43, 43, 43), hoverColour=(50, 50, 50), pressedColour=(100, 100, 100),
                         onClick=board.stop)
    slider = Slider(screen, 600, 180, 100, 20, min=25, initial=25)
    textbox = TextBox(screen, 600, 150, 75, 25, font=font, textColour='green', colour=(43, 43, 43),
                      borderThickness=0)
    textbox_speed = TextBox(screen, 600, 220, 75, 25, font=font, textColour='green', colour=(43, 43, 43),
                            borderThickness=0)
    speed_slider = Slider(screen, 600, 250, 100, 20, min=10, max=60, initial=30)
    textbox.setText('Board size:')
    textbox_speed.setText('Speed:')
    textbox.disable()
    textbox_speed.disable()
    while running:
        screen.fill((43, 43, 43))
        events = pygame.event.get()
        pygame_widgets.update(events)
        if board.width != slider.value:
            board.set_size(slider.value)
        if fps != speed_slider.value:
            fps = speed_slider.value
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.get_click(event.pos)
                if event.button == 4:
                    update_board = True
        if update_board or board.updating:
            board.update()
            update_board = False
        board.render(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
