from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from play import *
from level import *
from rank import *


janela = Window(800,600)
janela.set_title("Space Invaders")
fundo = GameImage("assets/images/background.png")

keyboard = Window.get_keyboard()
mouse = Window.get_mouse()

play = Sprite("assets/images/play.png")
play.x = janela.width/2 - play.width/2
play.y = 200

level = Sprite("assets/images/level.png")
level.x = janela.width/2 - play.width/2
level.y = 200 + play.height + 30

rank = Sprite("assets/images/rank.png")
rank.x = janela.width/2 - play.width/2
rank.y = level.y + 30 + level.height

exit = Sprite("assets/images/exit.png")
exit.x = janela.width/2 - play.width/2
exit.y = rank.y + 30 + rank.height

while True:

    if mouse.is_over_area([play.x, play.y], [play.x+play.width, play.y+play.height]) and mouse.is_button_pressed(1):
        Play(1)
    if mouse.is_over_area([level.x, level.y], [level.x + level.width, level.y + level.height]) and mouse.is_button_pressed(1):
        x = Level()
        print(x)
        Play(x)
    if mouse.is_over_area([rank.x, rank.y], [rank.x + rank.width, rank.y + rank.height]) and mouse.is_button_pressed(1):
        Rank()
    if mouse.is_over_area([exit.x, exit.y], [exit.x + exit.width, exit.y + exit.height]) and mouse.is_button_pressed(1):
        janela.close()

    fundo.draw()
    play.draw()
    level.draw()
    rank.draw()
    exit.draw()
    janela.update()