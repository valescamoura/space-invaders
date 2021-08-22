from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from functools import cmp_to_key

def cmp_score(score1, score2) -> int:
    if int(score1[1]) >= int(score2[1]):
        return -1
    else:
        return 1

def Formatar(lista) -> list:

    maior = 0
    for j in range(5):
        if len(lista[j][0]) > maior:
            maior = len(lista[j][0])
    for z in range(5):
        if len(lista[z][0]) != maior:
            lista[z][0] = lista[z][0] + ' '* 2 *(maior-len(lista[z][0]))
    maior = 0
    for j in range(5):
        if len(lista[j][1]) > maior:
            maior = len(lista[j][1])
    for z in range(5):
        if len(lista[z][1]) != maior:
            lista[z][1] = ' ' * 2 * (maior - len(lista[z][1])) + lista[z][1]
    return lista

def Rank() -> None:
    janela = Window(800,600)
    janela.set_title("Space Invaders")
    fundo = GameImage("assets/images/fundo.jpg")
    nome = Sprite("assets/images/rank.png")
    nome.x = janela.width/2 - nome.width/2

    keyboard = Window.get_keyboard()

    arquivo = open("assets/data/arquivo.txt", "r")
    rank = []
    for linha in arquivo:
       linha = linha.rstrip('\n')
       rank.append(linha.split('\t'))
    arquivo.close()

    '''for linha in rank:
        print(linha)'''

    rank.sort(key=cmp_to_key(cmp_score))
    rank = Formatar(rank)

    while True:
        fundo.draw()
        #nome.draw()
        janela.draw_text("RANK", 300, 20, size=86, color=(255, 255, 0))
        janela.draw_text('Player:         Score:', 245, 200, size=46, color=(255, 255, 0))
        janela.draw_text('  '.join(rank[0]), 245, 250, size=46, color=(255, 255, 255))
        janela.draw_text('  '.join(rank[1]), 245, 300, size=46, color=(255, 255, 255))
        janela.draw_text('  '.join(rank[2]), 245, 350, size=46, color=(255, 255, 255))
        janela.draw_text('  '.join(rank[3]), 245, 400, size=46, color=(255, 255, 255))
        janela.draw_text('  '.join(rank[4]), 245, 450, size=46, color=(255, 255, 255))

        janela.update()

        if keyboard.key_pressed("esc"):
            break
