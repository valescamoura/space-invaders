from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.collision import *
from rank import *
import random

def Play(game_speed, pontuacao=0) -> int:

    janela = Window(800, 600)
    janela.set_title("Space Invaders")
    fundo = GameImage("assets/images/fundo.jpg")

    keyboard = Window.get_keyboard()

    while game_speed <= 2:

        ### NAVE ###
        nave = Sprite("assets/images/ship.png")
        nave.y = janela.height - nave.height
        nave.x = janela.width/2 - nave.width/2
        #vel_nave = 200 * janela.delta_time()
        lista_de_tiros = []
        delta_t = 1
        #velocidade_tiro = -200 * janela.delta_time()

        ### FPS ###
        fps = 0
        contador_fps = 0
        tempo_transcorrido = 0

        ### MATRIZ DE NAVES INIMIGAS ###
        matriz = []
        x = -36
        y = 2
        vel_inimigo = 100

        for i in range(int(4*game_speed*1.5)):
            lista = []
            for j in range(6):
                inimigo = Sprite("assets/images/yellow_enemy.png")
                inimigo.x = x + inimigo.width + 2
                x = inimigo.x
                inimigo.y = y

                lista.append(inimigo)

            _ = Sprite("assets/images/yellow_enemy.png")
            matriz.append(lista)
            x = -36
            y += 1 + _.height

        lista_tiros_inim = []
        tempo_tiro = 0


        inimigos = 0
        vida = 5
        perdeu = 0
        digitou = 0
        time_won = 6
        nave_aleat = Sprite("assets/images/red_enemy.png")
        nave_aleat.x = - nave_aleat.width
        aleat = random.randint(600, 3600)

        while True:
            tempo_transcorrido += janela.delta_time()
            contador_fps += 1
            delta_t += janela.delta_time() #Tempo do tiro da nave
            tempo_tiro += janela.delta_time() #Tempo do tiro do inimigo
            aleat -= 1

            #NAVE ALEATORIA
            if aleat <= 0:
                if nave_aleat.x <= janela.width:
                    nave_aleat.x += 3
                else:
                    nave_aleat.x = -nave_aleat.width
                    aleat = random.randint(600, 3600)
                for z in range(len(lista_de_tiros)):
                    if lista_de_tiros[z].collided(nave_aleat):
                        pontuacao += 500
                        nave_aleat.x = -nave_aleat.width
                        lista_de_tiros.pop(z)
                        aleat = random.randint(600, 3600)
                        break


            # TEMPO TRANSCORRIDO - FPS
            if tempo_transcorrido >= 1:
                fps = contador_fps
                contador_fps = 0
                tempo_transcorrido = 0

            #MOVER NAVE
            if keyboard.key_pressed("right") and nave.x <= janela.width - nave.width and perdeu == 0:
                nave.x += 3
            if keyboard.key_pressed("left") and nave.x >= 0 and perdeu == 0:
                nave.x -= 3

            #TIRO DA NAVE
            if keyboard.key_pressed("space") and delta_t/game_speed >= 0.2 and perdeu == 0:
                tiro = Sprite("assets/images/bullet_player.png")
                tiro.x = nave.x - tiro.width/2 + nave.width/2
                tiro.y = janela.height - nave.height - tiro.height
                lista_de_tiros.append(tiro)
                delta_t = 0
            if not lista_de_tiros == [] and lista_de_tiros[0].y < 0:
                lista_de_tiros.pop(0)

            #MOVIMENTAR INIMIGOS
            for i in range(int(4*game_speed*1.5)):
                for j in range(6):
                    if matriz[i][j] != 0 and perdeu == 0:
                        matriz[i][j].move_x(vel_inimigo*janela.delta_time())

            x1 = 0
            y1 = 0
            x2 = 0
            y2 = 0
            temp1 = 0
            temp2 = 0

            for i in range(6):
                for j in range(int(4*game_speed*1.5)-1, -1, -1):
                    if matriz[j][i] != 0:
                        x1 = j
                        y1 = i
                        temp1 = 1
                    if temp1 != 0:
                        break
                if temp1 != 0:
                    break
            for i in range(5, -1, -1):
                for j in range(int(4*game_speed*1.5)-1, -1, -1):
                    if matriz[j][i] != 0:
                        x2 = j
                        y2 = i
                        temp2 = 1
                    if temp2 != 0:
                        break
                if temp2 != 0:
                    break

            if matriz[x1][y1] != 0 and perdeu == 0:
                if matriz[x1][y1].x <= 0 or matriz[x2][y2].x >= janela.width - matriz[x2][y2].width:
                    vel_inimigo *= -1
                    for i in range(int(4*game_speed*1.5)):
                        for j in range(6):
                            if matriz[i][j] != 0:
                                matriz[i][j].move_y(20)

            # TIRO DO INIMIGO
            x_aleat = random.randint(0, int(4*game_speed*1.5)-1)
            y_aleat = random.randint(0, 5)
            if matriz[x_aleat][y_aleat] != 0 and tempo_tiro * game_speed >= 1.5 and perdeu == 0:
                tiro = Sprite("assets/images/bullet_player.png")
                tiro.x = matriz[x_aleat][y_aleat].x - tiro.width / 2 + matriz[x_aleat][y_aleat].width / 2
                tiro.y = matriz[x_aleat][y_aleat].y + matriz[x_aleat][y_aleat].height
                lista_tiros_inim.append(tiro)
                tempo_tiro = 0
            if lista_tiros_inim != [] and lista_tiros_inim[0].y > janela.height:
                lista_tiros_inim.pop(0)

            #COLISAO TIRO DA NAVE COM INIMIGO
            if lista_de_tiros != [] and matriz[x1][y1] != 0 and perdeu == 0:
                if lista_de_tiros[0].y <= matriz[x1][y1].y or lista_de_tiros[0].y <= matriz[x2][y2].y or (lista_de_tiros[0].x >= matriz[x1][y1].x and lista_de_tiros[0].x <= matriz[x2][y2].x):
                    for i in range(int(4*game_speed*1.5)-1, -1, -1):
                        for j in range(5, -1, -1):
                            for z in range(len(lista_de_tiros)):
                                if matriz[i][j] != 0 and matriz[i][j].collided(lista_de_tiros[z]):
                                    matriz[i][j] = 0
                                    pontuacao += 100
                                    lista_de_tiros.pop(z)
                                    inimigos += 1
                                    break

            #COLISAO TIRO DO INIMIGO COM NAVE
            if lista_tiros_inim != [] and perdeu == 0:
                for z in range(len(lista_tiros_inim)):
                    if lista_tiros_inim[z].collided(nave):
                        lista_tiros_inim.pop(z)
                        vida -= 1
                        break

            #VOLTAR AO MENU INICIAL
            if keyboard.key_pressed("esc"):
                return 0

            ### UPDATE ###
            fundo.draw()
            janela.draw_text("FPS:"+str(fps), janela.width-90, janela.height-35, size=20, color=(255, 255, 255))
            janela.draw_text("Life:" + str(vida), janela.width - 80, 0, size=28, color=(255, 255, 255))
            janela.draw_text("Score:" + str(pontuacao), 10, 0, size=28, color=(255, 255, 255))
            nave.draw()
            nave_aleat.draw()
            if matriz != []:
                for i in range(int(4*game_speed*1.5)):
                    for j in range(6):
                        if matriz[i][j] != 0:
                            matriz[i][j].draw()
            if lista_de_tiros != []:
                for i in range(len(lista_de_tiros)):
                    lista_de_tiros[i].draw()

            if lista_tiros_inim != []:
                for i in range(len(lista_tiros_inim)):
                    lista_tiros_inim[i].draw()

            # GANHOU - PROXIMO NIVEL
            if inimigos == int(4*game_speed*1.5) * 6:
                time_won -= janela.delta_time()
                janela.draw_text("YOU WON!!!", 265, 250, size=68, color=(255, 255, 0))
            if time_won <= 0:
                game_speed += 0.5
                break

            janela.update()

            #ATUALIZAR POSIÇÃO DO TIRO DA NAVE
            for i in range(len(lista_de_tiros)):
                lista_de_tiros[i].y -= 5

            #ATUALIZAR POSIÇÃO DO TIRO DO INIMIGO
            for i in range(len(lista_tiros_inim)):
                lista_tiros_inim[i].y += 5

            #PERDEU
            if matriz[x1][y1] != 0 and matriz[x2][y2] != 0:
                if vida <= 0 or nave.y <= matriz[x1][y1].y + matriz[x1][y1].height or nave.y <= matriz[x2][y2].y + matriz[x2][y2].height:
                    perdeu = 1

            if perdeu == 1 and digitou == 0:
                janela.draw_text("GAME OVER!", 255, 250, size=68, color=(255, 255, 0))
                janela.draw_text("Digite seu nome (max=10 caract.) para ser registrado no RANK:", 200, 320, size=20, color=(255, 255, 255))
                print("Digite seu nome (max=10 caract.) para ser registrado no RANK:")
                janela.update()
                digitou = 1
                arquivo = open("assets/data/arquivo.txt", "a")
                nome = input()
                arquivo.write(nome+'\t'+str(pontuacao)+'\n')
                arquivo.close()

            if digitou == 1:
                Rank()
                return 0

    janela.draw_text("YOU WON!!!", 265, 250, size=68, color=(255, 255, 0))
    janela.draw_text("Digite seu nome (max=10 caract.) para ser registrado no RANK:", 200, 320, size=20, color=(255, 255, 255))
    print("Digite seu nome (max=10 caract.) para ser registrado no RANK:")
    janela.update()
    arquivo = open("assets/data/arquivo.txt", "a")
    nome = input()
    arquivo.write(nome + '\t' + str(pontuacao) + '\n')
    arquivo.close()
    Rank()
