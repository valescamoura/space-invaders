from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from play import *

def Level() -> float:

    janela = Window(800, 600)
    janela.set_title("Space Invaders")
    janela.set_background_color([0, 0, 0])
    fundo = GameImage("assets/images/background.png")

    level1 = Sprite("assets/images/level1.png")
    level1.x = janela.width / 2 - level1.width / 2
    level1.y = 200

    level2 = Sprite("assets/images/level2.png")
    level2.x = janela.width / 2 - level2.width / 2
    level2.y = 200 + level1.height + 30

    level3 = Sprite("assets/images/level3.png")
    level3.x = janela.width / 2 - level3.width / 2
    level3.y = level2.y + 30 + level2.height

    mouse = Window.get_mouse()
    keyboard = Window.get_keyboard()

    while True:
    
        if mouse.is_over_area([level1.x, level1.y], [level1.x + level1.width, level1.y + level1.height]) and mouse.is_button_pressed(1):
            return 1.0
        if mouse.is_over_area([level2.x, level2.y], [level2.x + level2.width, level2.y + level2.height]) and mouse.is_button_pressed(1):
            return 1.5
        if mouse.is_over_area([level3.x, level3.y], [level3.x + level3.width, level3.y + level3.height]) and mouse.is_button_pressed(1):
            return 2.0
        if keyboard.key_pressed("esc"):
            break

        fundo.draw()
        level1.draw()
        level2.draw()
        level3.draw()
        janela.update()