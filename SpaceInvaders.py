from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.sound import *
import random

random.seed()

game_speed = 1
game_state = 0

window = Window(400,600)
window.set_title("Space Invaders")
window.set_background_color([0,0,0])

while True:
    window.set_background_color([0,0,0])
    window.update()

fps = 0
contador = 0
tempo_transcorrido = 0
tempo_transcorrido += janela.delta_time()
contador += 1
# TEMPO TRANSCORRIDO
if tempo_transcorrido >= 1:
    fps = contador
    contador = 0
    tempo_transcorrido = 0
