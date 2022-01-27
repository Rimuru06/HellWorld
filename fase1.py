from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from random import randint

def fase1(janela, teclado, modulo, nivelDificuldade):
     cenario = Sprite("cenario.jpg", 1)
     chao = Sprite("chao.jpg", 1)
     chao.y = cenario.height
     player = Animation("player_idle.png", 4, True)
     player.set_sequence_time(0, 3, 240)
     chao.y = cenario.height
     player.x = 100
     player.y = chao.y - player.height
     playerx = 0
     playery = 0
     ativo = 0
     apertou = False
     tempoTrocaSprite = 0
     timerJump = 0
     velJump = 400
     velPlayer = 300
     velZumbi = 80
     velTiro = 500
     jump = False
     changeDJump = False
     alturaJump = player.y - 2.5*player.height
     fps = pygame.time.Clock()
     projeteisPlayerFrente = []
     projeteisPlayerTras = []
     playerVoltadoPraFrente = True
     timerTiro = 0
     playerAtirou = False
     etapaFase = 1
     vidasPlayer = 10
     listaZumbisEsquerda = []
     listaZumbisDireita = []
     playerMovimentar = True
     timerFase = 0
     timerSpwanZumbi = 0
     faseAcabou = False
     random = 0
     timerFimDaFase = 3
     playerMovendoDireita = False
     removerZumbi = False

     while modulo == 2:
          tempoTrocaSprite += janela.delta_time()
          if playerMovendoDireita == True:
               apertou = True
               player.x += velPlayer*janela.delta_time()
               if ativo != 1:
                    playerx = player.x
                    playery = player.y
                    player = Animation("player_run.png", 12, True)
                    player.set_sequence_time(0, 9, 90)
                    player.x = playerx
                    player.y = playery
                    ativo = 1
                    playerVoltadoPraFrente = True
               playerMovendoDireita = False
          if tempoTrocaSprite >= 0.6 and not apertou:
               tempoTrocaSprite = 0
               if ativo == 2:
                    playerx = player.x
                    playery = player.y
                    player = Animation("player_idle2.png", 4, True)
                    player.set_sequence_time(0, 3, 240)
                    player.x = playerx
                    player.y = playery
                    ativo = 0
               if ativo == 1:
                    playerx = player.x
                    playery = player.y
                    player = Animation("player_idle.png", 4, True)
                    player.set_sequence_time(0, 3, 240)
                    player.x = playerx
                    player.y = playery
                    ativo = 0
          apertou = False
          if playerMovimentar == True:
               if teclado.key_pressed("ESC"):
                    modulo = 1
               if teclado.key_pressed("RIGHT"):
                    playerMovendoDireita = True
               elif teclado.key_pressed("LEFT"):
                    apertou = True
                    player.x -= velPlayer*janela.delta_time()
                    if ativo != 2:
                         playerx = player.x
                         playery = player.y
                         player = Animation("player_run2.png", 10, True)
                         player.set_sequence_time(0, 9, 90)
                         player.x = playerx
                         player.y = playery
                         ativo = 2
                         playerVoltadoPraFrente = False

               if (teclado.key_pressed("UP")) and (jump == False):
                    apertou = True
                    jump = True
                    changeDJump = False
                    alturaJump = player.y - player.height
                    timerJump = 0
                    velJump = 400
               if jump == True:
                    timerJump += janela.delta_time()
                    if changeDJump == False:
                         player.y -= velJump*janela.delta_time()
                         if timerJump > 0.01:
                              velJump -= 10
                              timerJump = 0
                    if changeDJump == True:
                         player.y += velJump*janela.delta_time()
                         if timerJump > 0.01:
                              velJump += 10
                              timerJump = 0
               if player.y <= alturaJump:
                    changeDJump = True
               elif player.y + player.height >= chao.y:
                    jump = False
                    changeDJump = False
               
               if (teclado.key_pressed("SPACE")) and (playerAtirou == False):
                    playerAtirou = True
                    if playerVoltadoPraFrente == True:
                         tiroPlayer = Sprite("tiroPlayer.png", 1)
                         tiroPlayer.y = player.y + 30
                         tiroPlayer.x = player.x + player.width
                         projeteisPlayerFrente.append(tiroPlayer)
                    elif playerVoltadoPraFrente == False:
                         tiroPlayer = Sprite("tiroPlayer.png", 1)
                         tiroPlayer.y = player.y + 30
                         tiroPlayer.x = player.x
                         projeteisPlayerTras.append(tiroPlayer)
               
               if playerAtirou == True:
                    timerTiro += janela.delta_time()
                    if timerTiro > 0.2:
                         playerAtirou = False
                         timerTiro = 0
     
          cenario.draw()
          chao.draw()

          for t in range(len(projeteisPlayerFrente)-1, -1, -1):
               projeteisPlayerFrente[t].draw()
               projeteisPlayerFrente[t].x += velTiro*janela.delta_time()
               if projeteisPlayerFrente[t].x > janela.width:
                    projeteisPlayerFrente.remove(projeteisPlayerFrente[t])     
          for t in range(len(projeteisPlayerTras)-1, -1, -1):
               projeteisPlayerTras[t].draw()
               projeteisPlayerTras[t].x -= velTiro*janela.delta_time()
               if projeteisPlayerTras[t].x < 0:
                    projeteisPlayerTras.remove(projeteisPlayerTras[t])
          for z in range(len(listaZumbisDireita)-1, -1, -1):
               listaZumbisDireita[z].x += velZumbi*janela.delta_time()
               listaZumbisDireita[z].draw()
               for t in range(len(projeteisPlayerFrente)-1, -1, -1):
                    if listaZumbisDireita[z].collided(projeteisPlayerFrente[t]):
                         projeteisPlayerFrente.remove(projeteisPlayerFrente[t])
                         removerZumbi = True
               for t in range(len(projeteisPlayerTras)-1, -1, -1):
                    if listaZumbisDireita[z].collided(projeteisPlayerTras[t]):
                         projeteisPlayerTras.remove(projeteisPlayerTras[t])
                         removerZumbi = True
               if listaZumbisDireita[z].x > janela.width - listaZumbisDireita[z].width:
                    zumbiy = listaZumbisDireita[z].y
                    zumbix = listaZumbisDireita[z].x
                    removerZumbi = True
                    zumbi = Sprite("zumbiEsquerda.png", 1)
                    zumbi.y = zumbiy
                    zumbi.x = zumbix
                    listaZumbisEsquerda.append(zumbi)
               if removerZumbi == True:
                    listaZumbisDireita.remove(listaZumbisDireita[z])
                    removerZumbi = False
          for z in range(len(listaZumbisEsquerda)-1, -1, -1): 
               listaZumbisEsquerda[z].x -= velZumbi*janela.delta_time()
               listaZumbisEsquerda[z].draw()
               for t in range(len(projeteisPlayerFrente)-1, -1, -1):
                    if listaZumbisEsquerda[z].collided(projeteisPlayerFrente[t]):
                         projeteisPlayerFrente.remove(projeteisPlayerFrente[t])
                         removerZumbi = True
               for t in range(len(projeteisPlayerTras)-1, -1, -1):
                    if listaZumbisEsquerda[z].collided(projeteisPlayerTras[t]):
                         projeteisPlayerTras.remove(projeteisPlayerTras[t])
                         removerZumbi = True
               if listaZumbisEsquerda[z].x < 0 + listaZumbisEsquerda[z].width:
                    zumbiy = listaZumbisEsquerda[z].y
                    zumbix = listaZumbisEsquerda[z].x
                    listaZumbisEsquerda.remove(listaZumbisEsquerda[z])
                    zumbi = Sprite("zumbiDireita.png", 1)
                    zumbi.y = zumbiy
                    zumbi.x = zumbix
                    listaZumbisDireita.append(zumbi)  
               if removerZumbi == True:
                    listaZumbisEsquerda.remove(listaZumbisEsquerda[z])
                    removerZumbi = False

          if etapaFase == 1:
               if player.x > janela.width:
                    etapaFase = 1.5
                    player.x = 0 - player.width*3
                    playerMovimentar = False
          elif etapaFase == 1.5:
               playerMovendoDireita = True
               if player.x >= janela.width/2 - player.width:
                    etapaFase = 2
                    playerMovimentar = True
                    timerFase = 0
                    timerSpwanZumbi = 0
                    timerFimDaFase = 0
          elif etapaFase == 2:
               timerFase += janela.delta_time()
               timerSpwanZumbi += janela.delta_time()
               if (etapaFase < 60) and (timerSpwanZumbi > 1/nivelDificuldade):
                    random = randint(1, 3)
                    timerSpwanZumbi = 0
                    if random == 1:
                         zumbi = Sprite("zumbiDireita.png", 1)
                         zumbi.y = chao.y - zumbi.height
                         zumbi.x = 0 - zumbi.width
                         listaZumbisDireita.append(zumbi)
                    elif random == 2:
                         zumbi = Sprite("zumbiEsquerda.png", 1)
                         zumbi.y = chao.y - zumbi.height
                         zumbi.x = janela.width + zumbi.width
                         listaZumbisEsquerda.append(zumbi)
               elif (etapaFase > 60) and (len(listaZumbisDireita==0)) and (len(listaZumbisEsquerda==0)):
                    timerFimDaFase += janela.delta_time()
               if timerFimDaFase > 3:
                    faseAcabou = True
                    playerMovimentar = False
               if faseAcabou == True:
                    playerMovendoDireita = True
               if (faseAcabou == True) and (player.x > janela.width):
                    etapaFase = 2.5
                    player.x = 0 - player.width*1.5
          elif etapaFase == 2.5:
               playerMovendoDireita = True
               if player.x >= janela.width/2 - player.width:
                    etapaFase = 2
                    playerMovimentar = True
                    timerFase = 0
                    timerSpwanZumbi = 0
                    timerFimDaFase = 0

          elif etapaFase == 3:
               timerFase += janela.delta_time()
               timerSpwanZumbi += janela.delta_time()
               if (etapaFase < 120) and (timerSpwanZumbi > 0.3/nivelDificuldade):
                    random = randint(1, 3)
                    if random == 1:
                         zumbi = Sprite("zumbiDireita.png", 1)
                         zumbi.y = chao.y - zumbi.height
                         zumbi.x = 0 - zumbi.width
                         listaZumbisDireita.append(zumbi)
                    elif random == 2:
                         zumbi = Sprite("zumbiEsquerda.png", 1)
                         zumbi.y = chao.y - zumbi.height
                         zumbi.x = janela.width + zumbi.width
                         listaZumbisEsquerda.append(zumbi)
               elif (etapaFase > 120) and (len(listaZumbisDireita==0)) and (len(listaZumbisEsquerda==0)):
                    timerFimDaFase += janela.delta_time()
               if timerFimDaFase > 3:
                    faseAcabou = True
                    playerMovimentar = False
               if faseAcabou == True:
                    playerMovendoDireita = True
               if (faseAcabou == True) and (player.x > janela.width):
                    etapaFase = 2.5
                    player.x = 0 - player.width*1.5

          elif etapaFase == 3.5:
               playerMovendoDireita = True
               if player.x >= janela.width/2 - player.width:
                    etapaFase = 2
                    playerMovimentar = True
                    timerFase = 0
                    timerSpwanZumbi = 0
                    timerFimDaFase = 0

          elif etapaFase == 4:
               timerFase += janela.delta_time()
               timerSpwanZumbi += janela.delta_time()
               if (etapaFase < 180) and (timerSpwanZumbi > 0.1/nivelDificuldade):
                    random = randint(1, 3)
                    if random == 1:
                         zumbi = Sprite("zumbiDireita.png", 1)
                         zumbi.y = chao.y - zumbi.height
                         zumbi.x = 0 - zumbi.width
                         listaZumbisDireita.append(zumbi)
                    elif random == 2:
                         zumbi = Sprite("zumbiEsquerda.png", 1)
                         zumbi.y = chao.y - zumbi.height
                         zumbi.x = janela.width + zumbi.width
                         listaZumbisEsquerda.append(zumbi)
               elif (etapaFase > 180) and (len(listaZumbisDireita==0)) and (len(listaZumbisEsquerda==0)):
                    timerFimDaFase += janela.delta_time()
               if timerFimDaFase > 3:
                    faseAcabou = True
                    playerMovimentar = False
               if faseAcabou == True:
                    playerMovendoDireita = True
               if (faseAcabou == True) and (player.x > janela.width):
                    etapaFase = 2.5
                    player.x = 0 - player.width*1.5

          elif etapaFase == 4.5:
               playerMovendoDireita = True
               if player.x >= janela.width/2 - player.width:
                    etapaFase = 2
                    playerMovimentar = True
                    timerFase = 0
                    timerSpwanZumbi = 0
                    timerFimDaFase = 0


          player.draw()
          janela.draw_text("Vidas: " + str(vidasPlayer), 10, janela.height - 70, 30, (255, 0, 0), "Arial", True, False)
          player.update()
          janela.update()
          fps.tick(60)

          if vidasPlayer <= 0:
               modulo = 1
     
     return modulo