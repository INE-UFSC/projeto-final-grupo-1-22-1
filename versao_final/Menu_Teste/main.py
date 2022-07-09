import pygame as pg
import button

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Copper Temple")

game_paused = False
menu_state = "main"

font = pg.font.SysFont("arialblack", 40)

TEXT_COLOR = (255, 255, 255)

resume_img = pg.image.load("images/button_resume.png").convert_alpha()
options_img = pg.image.load("images/button_options.png").convert_alpha()
quit_img = pg.image.load("images/button_quit.png").convert_alpha()
video_img = pg.image.load("images/button_video.png").convert_alpha()
audio_img = pg.image.load("images/button_audio.png").convert_alpha()
keys_img = pg.image.load("images/button_keys.png").convert_alpha()
back_img = pg.image.load("images/button_back.png").convert_alpha()

resume_button = button.Button(304, 125, resume_img, 1)
options_button = button.Button(297, 250, options_img, 1)
quit_button = button.Button(336, 375, quit_img, 1)
video_button = button.Button(226, 75, video_img, 1)
audio_button = button.Button(225, 200, audio_img, 1)
keys_button = button.Button(246, 325, keys_img, 1)
back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True

while run:
    screen.fill((52, 78, 91))

    if game_paused == True:
        if menu_state == "main":
            if resume_button.draw(screen):
                game_paused = False
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                run = False

        if menu_state == "options":
            if video_button.draw(screen):
                print("Video Settings")
            if audio_button.draw(screen):
                print("Audio Settings")
            if keys_button.draw(screen):
                print("Change keys")
            if back_button.draw(screen):
                menu_state = "main"
    else:
        draw_text("Press SPACE to pause", font, TEXT_COLOR, 160, 250)

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                game_paused = True
        if event.type == pg.QUIT:
            run = False

    pg.display.update()

pg.quit()
