import pygame
import os
from time import sleep

grafic = "normal"
fps_True = True
full = False

# все функции


def load_image(name, data, colorkey=None):
    fullname = os.path.join(data, name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image
    return image


# все классы

class Fps:
    def __init__(self, fps_True):
        if fps_True == True:
            font = pygame.font.Font(None, 48)
            self.text = font.render(('tick = {}, fps = {}'.format(int(clock.tick(fps)), int(clock.get_fps()*5))), 0, (0, 0, 0))
            screen.blit(self.text, (0, 0))


class MainMenu:
    def __init__(self):
        # загрузка всех показателей
        font = pygame.font.Font(None, 48)
        self.textL = "Загрузка"
        self.loading = 'Загрузка текстур'
        self.process = 0
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))

        self.background0 = load_image("start_menu_background.png", "data")
        self.background0 = pygame.transform.scale(self.background0, size)
        screen.blit(self.background0, (0, 0))
        screen.blit(self.text, (0, 0))
        self.process = int(100 / col)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.background1 = load_image("start_menu_background_1.png", "data")
        self.background1 = pygame.transform.scale(self.background1, size_fone)
        self.process = int(100 / col * 2)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.play = load_image("button_play.png", "data")
        self.play = pygame.transform.scale(self.play, size_but)
        self.process = int(100 / col * 3)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.play1 = load_image("button_play.png", "data")
        self.play1 = pygame.transform.scale(self.play1, (size_but[0]+20, size_but[1]+20))
        self.process = int(100 / col * 4)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.setting = load_image("button_settings.png", "data")
        self.setting = pygame.transform.scale(self.setting, size_but)
        self.process = int(100 / col * 5)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.setting1 = load_image("button_settings.png", "data")
        self.setting1 = pygame.transform.scale(self.setting1, (size_but[0]+20, size_but[1]+20))
        self.process = int(100 / col * 6)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.exit = load_image("button_exit.png", "data")
        self.exit = pygame.transform.scale(self.exit, size_but)
        self.process = int(100 / col * 7)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.exit1 = load_image("button_exit.png", "data")
        self.exit1 = pygame.transform.scale(self.exit1, (size_but[0]+20, size_but[1]+20))
        self.process = int(100 / col * 8)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting = load_image("menu_settings.png", "data")
        self.menu_setting = pygame.transform.scale(self.menu_setting, (int(size[0]/3.67), int(size[1]/1.34)))
        self.process = int(100 / col * 9)
        screen.blit(self.background0, (size[0]/8.51, size[1]/22))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_back = load_image("menu_settings_back.png", "data")
        self.menu_setting_back = pygame.transform.scale(self.menu_setting_back, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 10)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_back1 = load_image("menu_settings_back.png", "data")
        self.menu_setting_back1 = pygame.transform.scale(self.menu_setting_back1, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 11)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_480 = load_image("menu_settings_480.png", "data")
        self.menu_setting_480 = pygame.transform.scale(self.menu_setting_480, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 12)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting1_480 = load_image("menu_settings_480.png", "data")
        self.menu_setting1_480 = pygame.transform.scale(self.menu_setting1_480, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 13)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_720 = load_image("menu_settings_720.png", "data")
        self.menu_setting_720 = pygame.transform.scale(self.menu_setting_720, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 14)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting1_720 = load_image("menu_settings_720.png", "data")
        self.menu_setting1_720 = pygame.transform.scale(self.menu_setting1_720, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 15)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_1080 = load_image("menu_settings_1080.png", "data")
        self.menu_setting_1080 = pygame.transform.scale(self.menu_setting_1080, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 16)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting1_1080 = load_image("menu_settings_1080.png", "data")
        self.menu_setting1_1080 = pygame.transform.scale(self.menu_setting1_1080, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 17)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_eazy = load_image("menu_settings_eazy.png", "data")
        self.menu_setting_eazy = pygame.transform.scale(self.menu_setting_eazy, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 18)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_eazy1 = load_image("menu_settings_eazy.png", "data")
        self.menu_setting_eazy1 = pygame.transform.scale(self.menu_setting_eazy1, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 19)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_normal = load_image("menu_settings_normal.png", "data")
        self.menu_setting_normal = pygame.transform.scale(self.menu_setting_normal, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 20)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_normal1 = load_image("menu_settings_normal.png", "data")
        self.menu_setting_normal1 = pygame.transform.scale(self.menu_setting_normal1, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 21)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_super = load_image("menu_settings_super.png", "data")
        self.menu_setting_super = pygame.transform.scale(self.menu_setting_super, (int(size[0]/6.47), int(size[1]/7.1)))
        self.process = int(100 / col * 22)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_super1 = load_image("menu_settings_super.png", "data")
        self.menu_setting_super1 = pygame.transform.scale(self.menu_setting_super1, (int(size[0]/6.47+20), int(size[1]/7.1+20)))
        self.process = int(100 / col * 23)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_full = load_image("menu_settings_full.png", "data")
        self.menu_setting_full = pygame.transform.scale(self.menu_setting_full, (int(size[0]/3.67), int(size[1]/9)))
        self.process = int(100 / col * 24)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_full1 = load_image("menu_settings_full.png", "data")
        self.menu_setting_full1 = pygame.transform.scale(self.menu_setting_full1, (int(size[0]/3.67+20), int(size[1]/9+20)))
        self.process = int(100 / col * 25)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_window = load_image("menu_settings_window.png", "data")
        self.menu_setting_window = pygame.transform.scale(self.menu_setting_window, (int(size[0]/3.67), int(size[1]/9)))
        self.process = int(100 / col * 26)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_window1 = load_image("menu_settings_window.png", "data")
        self.menu_setting_window1 = pygame.transform.scale(self.menu_setting_window1, (int(size[0]/3.67+20), int(size[1]/9+20)))
        self.process = int(100 / col * 27)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_off = load_image("menu_settings_off.png", "data")
        self.menu_setting_off = pygame.transform.scale(self.menu_setting_off, (int(size[0]/6.66), int(size[1]/6.66)))
        self.process = int(100 / col * 28)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_off1 = load_image("menu_settings_off.png", "data")
        self.menu_setting_off1 = pygame.transform.scale(self.menu_setting_off1, (int(size[0]/6.66+20), int(size[1]/6.66+20)))
        self.process = int(100 / col * 29)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_on = load_image("menu_settings_on.png", "data")
        self.menu_setting_on = pygame.transform.scale(self.menu_setting_on, (int(size[0]/6.66), int(size[1]/6.66)))
        self.process = int(100 / col * 30)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()
        self.menu_setting_on1 = load_image("menu_settings_on.png", "data")
        self.menu_setting_on1 = pygame.transform.scale(self.menu_setting_on1, (int(size[0]/6.66+20), int(size[1]/6.66+20)))
        self.process = int(100 / col * 31)
        screen.blit(self.background0, (0, 0))
        self.text = font.render(self.loading + " " + str(self.process) + "%", 0, (0, 0, 0))
        screen.blit(self.text, (0, 0))
        pygame.display.flip()

    def update(self, x1, y1):
        screen.blit(self.background0, (0, 0))
        screen.blit(self.background1, (-150 + x1, -150 + y1))
        Fps(fps_True)
        if menu == 1:
            screen.blit(self.menu_setting, (70, 60))
            global grafic
            if st == 1:
                screen.blit(self.menu_setting_back1, (width/10.3-10, height/1.19-10))
            else:
                screen.blit(self.menu_setting_back, (width/10.3, height/1.19))
            if bt == 0:
                screen.blit(self.menu_setting1_480, (size[0]/2.48, size[1]/8.7))
            else:
                screen.blit(self.menu_setting_480, (size[0]/2.48+10, size[1]/8.7+10))
            if bt == 1:
                screen.blit(self.menu_setting1_720, (size[0]/1.74, size[1]/8.7))
            else:
                screen.blit(self.menu_setting_720, (size[0]/1.74+10, size[1]/8.7+10))
            if bt == 2:
                screen.blit(self.menu_setting1_1080, (size[0]/1.28, size[1]/8.7))
            else:
                screen.blit(self.menu_setting_1080, (size[0]/1.28+10, size[1]/8.7+10))
            if kt == 0:
                screen.blit(self.menu_setting_eazy1, (size[0]/2.5, size[1]/3.67))
                grafic = "eazy"
            else:
                screen.blit(self.menu_setting_eazy, (size[0]/2.5+10, size[1]/3.67+10))
            if kt == 1:
                screen.blit(self.menu_setting_normal1, (size[0]/1.75, size[1]/3.67))
                grafic = "normal"
            else:
                screen.blit(self.menu_setting_normal, (size[0]/1.75+10, size[1]/3.67+10))
            if kt == 2:
                screen.blit(self.menu_setting_super1, (size[0]/1.28, size[1]/3.67))
                grafic = "super"
            else:
                screen.blit(self.menu_setting_super, (size[0]/1.28+10, size[1]/3.67+10))
            if full == True:
                screen.blit(self.menu_setting_full1, (size[0]/2.93+10, size[1]/2.05+10))
                screen.blit(self.menu_setting_window, (size[0]/1.5, size[1]/2.05))
            else:
                screen.blit(self.menu_setting_full, (size[0]/2.93, size[1]/2.05))
                screen.blit(self.menu_setting_window1, (size[0]/1.5+10, size[1]/2.05+10))
            if fps_True == True:
                screen.blit(self.menu_setting_on1, (size[0]/1.57+10, size[1]/1.63+10))
                screen.blit(self.menu_setting_off, (size[0]/2.61, size[1]/1.63))
            else:
                screen.blit(self.menu_setting_on, (size[0]/1.57, size[1]/1.63))
                screen.blit(self.menu_setting_off1, (size[0]/2.61+10, size[1]/1.63+10))
        if menu == 0:
            if st == 1:
                screen.blit(self.play1, (width/2-width2/2-10, height/10*3-height2-10))
            else:
                screen.blit(self.play, (width/2-width2/2, height/10*3-height2))
            if st == 2:
                screen.blit(self.setting1, (width/2-width2/2-10, height/10*6-height2-10))
            else:
                screen.blit(self.setting, (width/2-width2/2, height/10*6-height2))
            if st == 3:
                screen.blit(self.exit1, (width/2-width2/2-10, height/10*9-height2-10))
            else:
                screen.blit(self.exit, (width/2-width2/2, height/10*9-height2))

    def dplay(self):
        screen.blit(self.play1, (width/2-width2/2-10, height/10*3-height2-10))

    def dsetting(self):
        screen.blit(self.setting1, (width/2-width2/2-10, height/10*6-height2-10))

    def dclose(self):
        screen.blit(self.exit1, (width/2-width2/2-10, height/10*9-height2-10))

    def dback(self):
        screen.blit(self.menu_setting_back1, (width/10.3-10, height/1.19-10))

    def deazy(self):
        global grafic
        grafic = "eazy"

    def dnormal(self):
        global grafic
        grafic = "normal"

    def dsuper(self):
        global grafic
        grafic = "super"

    def d480(self):
        global size, width, height, size_command, size_fone, width1, width2, height1, height2, size_but, screen, main, bt
        try:
            screen = pygame.display.set_mode((920, 480), pygame.RESIZABLE | pygame.FULLSCREEN)
        except Exception:
            return 0
        if full == True:
            size = width, height = 920, 480
            size_command = 1
            size_fone = width1, height1 = int(size[0]*1.5), int(size[1]*1.5)
            size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.FULLSCREEN)
        else:
            size = width, height = 920, 480
            size_command = 1
            size_fone = width1, height1 = int(size[0]*1.5), int(size[1]*1.5)
            size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        main = MainMenu()
        bt = 0
        main.update(0, 0)

    def d720(self):
        global size, width, height, size_command, size_fone, width1, width2, height1, height2, size_but, screen, main, bt
        try:
            screen = pygame.display.set_mode((1360, 720), pygame.RESIZABLE | pygame.FULLSCREEN)
        except Exception:
            return 0
        if full == True:
            size = width, height = 1360, 765
            size_command = 1
            size_fone = width1, height1 = int(size[0]*1.5), int(size[1]*1.5)
            size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.FULLSCREEN)
        else:
            size = width, height = 1360, 765
            size_command = 1
            size_fone = width1, height1 = int(size[0]*1.5), int(size[1]*1.5)
            size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        main = MainMenu()
        bt = 1
        main.update(0, 0)

    def d1080(self):
        global size, width, height, size_command, size_fone, width1, width2, height1, height2, size_but, screen, main, bt
        try:
            screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.FULLSCREEN)
        except Exception:
            return 0
        if full == True:
            size = width, height = 1920, 1080
            size_command = 1
            size_fone = width1, height1 = int(size[0]*1.5), int(size[1]*1.5)
            size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.FULLSCREEN)
        else:
            size = width, height = 1920, 1080
            size_command = 1
            size_fone = width1, height1 = int(size[0]*1.5), int(size[1]*1.5)
            size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        main = MainMenu()
        bt = 2
        main.update(0, 0)

    def dfull(self):
        global size, screen, full
        full = True
        screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.FULLSCREEN)

    def dwindow(self):
        global size, screen, full
        full = False
        screen = pygame.display.set_mode(size, pygame.RESIZABLE)


pygame.init()
pygame.display.set_caption('Uncknow game')
pygame.display.set_icon(load_image("start_menu_background.png", "data"))
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
col = 31
st = 0
fps = 60
bt = 1
kt = 1
x, y = 0, 0
menu = 0
if full == True:
    size = width, height = 1360, 765
    size_command = 1
    size_fone = width1, height1 = int(size[0]*1.14), int(size[1]*1.18)
    size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE | pygame.FULLSCREEN)
else:
    size = width, height = 1360, 765
    size_command = 1
    size_fone = width1, height1 = int(size[0]*1.14), int(size[1]*1.18)
    size_but = width2, height2 = int(size[0]/2.72), int(size[1]/3.62)
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
pygame.display.flip()
main = MainMenu()
main.update(0, 0)
running = True
while running:
    main.update(x, y)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        if i.type == pygame.MOUSEMOTION:
            x, y = i.pos[0]/10, i.pos[1]/10
            if width/2-width2/2 < i.pos[0] < width/2+width2/2 and height/10*3 > i.pos[1] > height/10*3-height2-10 and menu == 0:
                st = 1
                main.dplay()
            elif width/2-width2/2 < i.pos[0] < width/2+width2/2 and height/10*6 > i.pos[1] > height/10*6-height2-10 and menu == 0:
                st = 2
                main.dsetting()
            elif width/2-width2/2 < i.pos[0] < width/2+width2/2 and height/10*9 > i.pos[1] > height/10*9-height2-10 and menu == 0:
                st = 3
                main.dclose()
            elif width/10.3 < i.pos[0] < width/10.3 + size[0] / 6.47 and height/1.19 < i.pos[1] < height/1.19 + size[1] / 7.1 and menu == 1:
                st = 1
                main.dback()
            else:
                st = 0
        if i.type == pygame.MOUSEBUTTONDOWN:
            if width/2-width2/2 < i.pos[0] < width/2+width2/2 and height/10*3 > i.pos[1] > height/10*3-height2-10 and menu == 0:
                pass
            if width/2-width2/2 < i.pos[0] < width/2+width2/2 and height/10*6 > i.pos[1] > height/10*6-height2-10 and menu == 0:
                menu = 1
                main.update(0, 0)
                pygame.display.flip()
                sleep(0.2)
            if width/2-width2/2 < i.pos[0] < width/2+width2/2 and height/10*9 > i.pos[1] > height/10*9-height2-10 and menu == 0:
                running = False
                break
            if width/10.3 < i.pos[0] < width/10.3 + size[0] / 6.47 and height/1.19 < i.pos[1] < height/1.19 + size[1] / 7.1 and menu == 1:
                menu = 0
            if size[0]/2.48 < i.pos[0] < size[0]/2.48 + size[0]/6.47 and size[1]/8.7 < i.pos[1] < size[1]/8.7 + size[1]/7.1 and menu == 1:
                main.d480()
            if size[0]/1.74 < i.pos[0] < size[0]/1.74 + size[0]/6.47 and size[1]/8.7 < i.pos[1] < size[1]/8.7 + size[1]/7.1 and menu == 1:
                main.d720()
            if size[0]/1.28 < i.pos[0] < size[0]/1.28 + size[0]/6.47 and size[1]/8.7 < i.pos[1] < size[1]/8.7 + size[1]/7.1 and menu == 1:
                main.d1080()
            if size[0] / 2.93 < i.pos[0] < size[0] / 2.93 + size[0] / 3.67 + 20 and size[1] / 2.05 < i.pos[1] < size[1] / 2.05 + size[1] / 9 + 20 and menu == 1:
                main.dfull()
            if size[0] / 1.5 < i.pos[0] < size[0] / 1.5 + size[0] / 5.71 and size[1] / 2.05 < i.pos[1] < size[1] / 2.05 + size[1] / 11 and menu == 1:
                main.dwindow()
            if size[0]/2.5 < i.pos[0] < size[0]/2.5 + size[0]/6.47 and size[1]/3.67 < i.pos[1] < size[1]/3.67 + size[1]/7.1:
                kt = 0
                main.deazy()
            if size[0]/1.75 < i.pos[0] < size[0]/1.75 + size[0]/6.47 and size[1]/3.67 < i.pos[1] < size[1]/3.67 + size[1]/7.1:
                kt = 1
                main.dnormal()
            if size[0]/1.28 < i.pos[0] < size[0]/1.28 + size[0]/6.47 and size[1]/3.67 < i.pos[1] < size[1]/3.67 + size[1]/7.1:
                kt = 2
                main.dsuper()
            if size[0]/1.57+10 < i.pos[0] < size[0]/1.57+10 + size[0]/6.66 and size[1]/1.63+10 < i.pos[1] < size[1]/1.63+10 + size[0]/6.66:
                fps_True = True
            if size[0]/2.61+10 < i.pos[0] < size[0]/2.61+10 + size[0]/6.66 and size[1]/1.63+10 < i.pos[1] < size[1]/1.63+10 + size[0]/6.66:
                fps_True = False
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
