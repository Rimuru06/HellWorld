from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from random import randint

def fase1(janela, teclado, modulo, nivelDificuldade, vidasPlayer):
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
     velFireDemon = 100
     velTiro = 600
     jump = False
     changeDJump = False
     alturaJump = player.y - 3*player.height
     fps = pygame.time.Clock()
     projeteisPlayerFrente = []
     projeteisPlayerTras = []
     playerVoltadoPraFrente = True
     timerTiro = 0
     playerAtirou = False
     etapaFase = 1
     listaZumbisEsquerda = []
     listaZumbisDireita = []
     listaFireDemons = []
     playerMovimentar = True
     timerFase = 0
     timerSpwanZumbi = 0
     timerSpwanFireDemon = 0
     faseAcabou = False
     random = 0
     timerFimDaFase = 1
     playerMovendoDireita = False
     removerZumbi = False
     playerIntangivel = False
     timerIntangivel = 0
     timerPiscando = 0
     playerPiscar = 1
     removerFireDemon = False

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
                    alturaJump = player.y - 3*player.height
                    timerJump = 0
                    velJump = 400
               
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
                    if timerTiro > 0.25:
                         playerAtirou = False
                         timerTiro = 0
          if jump == True:
               timerJump += janela.delta_time()
               if changeDJump == False:
                    player.y -= velJump*janela.delta_time()
                    if timerJump > 0.01:
                         velJump -= 20
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
               if (listaZumbisDireita[z].collided(player)) and (playerIntangivel == False):
                    vidasPlayer -= 1
                    playerIntangivel = True
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
               if (listaZumbisEsquerda[z].collided(player)) and (playerIntangivel == False):
                    vidasPlayer -= 1
                    playerIntangivel = True
               for t in range(len(projeteisPlayerFrente)-1, -1, -1):
                    if listaZumbisEsquerda[z].collided(projeteisPlayerFrente[t]):
                         projeteisPlayerFrente.remove(projeteisPlayerFrente[t])
                         removerZumbi = True
               for t in range(len(projeteisPlayerTras)-1, -1, -1):
                    if listaZumbisEsquerda[z].collided(projeteisPlayerTras[t]):
                         projeteisPlayerTras.remove(projeteisPlayerTras[t])
                         removerZumbi = True
               if listaZumbisEsquerda[z].x < 0:
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
          for z in range(len(listaFireDemons)-1, -1, -1):
               if listaFireDemons[z].y < chao.y - player.height:
                    if listaFireDemons[z].x < player.x:
                         listaFireDemons[z].x += velFireDemon*janela.delta_time()/3
                         listaFireDemons[z].y += velFireDemon*janela.delta_time()
                    elif listaFireDemons[z].x > player.x:
                         listaFireDemons[z].y += velFireDemon*janela.delta_time()
                         listaFireDemons[z].x -= velFireDemon*janela.delta_time()/3
               else:
                    if listaFireDemons[z].x < player.x:
                         listaFireDemons[z].x += 7*velFireDemon*janela.delta_time()
                    elif listaFireDemons[z].x > player.x:
                         listaFireDemons[z].x -= 7*velFireDemon*janela.delta_time()
               listaFireDemons[z].draw()
               if (listaFireDemons[z].collided(player)) and (playerIntangivel == False):
                    vidasPlayer -= 1
                    playerIntangivel = True
                    removerFireDemon = True
               for t in range(len(projeteisPlayerFrente)-1, -1, -1):
                    if listaFireDemons[z].collided(projeteisPlayerFrente[t]):
                         projeteisPlayerFrente.remove(projeteisPlayerFrente[t])
                         removerFireDemon = True
               for t in range(len(projeteisPlayerTras)-1, -1, -1):
                    if listaFireDemons[z].collided(projeteisPlayerTras[t]):
                         projeteisPlayerTras.remove(projeteisPlayerTras[t])
                         removerFireDemon = True
               if removerFireDemon == True:
                    listaFireDemons.remove(listaFireDemons[z])
                    removerFireDemon = False

          if etapaFase == 1:
               if player.x > janela.width:
                    etapaFase = 1.5
                    player.x = 0 - player.width*3
                    playerMovimentar = False
                    janela.clear()
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
               if (timerFase < 20) and (timerSpwanZumbi > 0.3/nivelDificuldade):
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
               elif (timerFase > 20) and (len(listaZumbisDireita)==0) and (len(listaZumbisEsquerda)==0):
                    timerFimDaFase += janela.delta_time()
               if timerFimDaFase > 0.5:
                    faseAcabou = True
                    playerMovimentar = False
               if faseAcabou == True:
                    playerMovendoDireita = True
               if (faseAcabou == True) and (player.x > janela.width):
                    etapaFase = 2.5
                    player.x = 0 - player.width*1.5
                    janela.clear()
          elif etapaFase == 2.5:
               playerMovendoDireita = True
               if player.x >= janela.width/2 - player.width:
                    etapaFase = 3
                    playerMovimentar = True
                    timerFase = 0
                    timerSpwanZumbi = 0
                    timerSpwanFireDemon = 0
                    timerFimDaFase = 0
                    playerMovendoDireita = False
                    faseAcabou = False
                    vidasPlayer += 1
          elif etapaFase == 3:
               timerFase += janela.delta_time()
               timerSpwanZumbi += janela.delta_time()
               timerSpwanFireDemon += janela.delta_time()
               if (timerFase < 40) and (timerSpwanZumbi > 0.4/nivelDificuldade):
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
               elif (timerFase < 40) and (timerSpwanFireDemon > 1/nivelDificuldade):
                    timerSpwanFireDemon = 0
                    random = randint(0, janela.width-50)
                    fireDemon = Sprite("fireDemon.png", 1)
                    fireDemon.y = 0 - fireDemon.height
                    fireDemon.x = random
                    listaFireDemons.append(fireDemon)
               elif (timerFase > 10) and (len(listaZumbisDireita)==0) and (len(listaZumbisEsquerda)==0) and (len(listaFireDemons)==0):
                    timerFimDaFase += janela.delta_time()
               if timerFimDaFase > 0.5:
                    faseAcabou = True
                    playerMovimentar = False
               if faseAcabou == True:
                    playerMovendoDireita = True
               if (faseAcabou == True) and (player.x > janela.width):
                    etapaFase = 3.5
                    player.x = 0 - player.width*1.5
                    janela.clear()

          elif etapaFase == 3.5:
               playerMovendoDireita = True
               if player.x >= janela.width/2 - player.width:
                    etapaFase = 4
                    playerMovimentar = True
                    timerFase = 0
                    timerSpwanZumbi = 0
                    timerSpwanFireDemon = 0
                    timerSpwanFireDemon = 0
                    timerFimDaFase = 0
                    playerMovendoDireita = False
                    faseAcabou = False
                    vidasPlayer += 1

          elif etapaFase == 4:
               timerFase += janela.delta_time()
               timerSpwanZumbi += janela.delta_time()
               timerSpwanFireDemon += janela.delta_time()
               if (timerFase < 60) and (timerSpwanZumbi > 0.4/nivelDificuldade):
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
               elif (timerFase < 60) and (timerSpwanFireDemon > 0.8/nivelDificuldade):
                    timerSpwanFireDemon = 0
                    random1 = randint(1,4)
                    fireDemon = Sprite("fireDemon.png", 1)
                    if random1 == 1:
                         random2 = randint(0, int(player.y))
                         fireDemon.x = 0 - fireDemon.width
                         fireDemon.y = random2
                    elif random1 == 2:
                         random2 = randint(-50, janela.width+1)
                         fireDemon.y = 0 - fireDemon.height
                         fireDemon.x = random2
                    elif random1 == 3:
                         random2 = randint(0, int(player.y))
                         fireDemon.x = janela.width
                         fireDemon.y = random2
                    listaFireDemons.append(fireDemon)
               elif (timerFase > 10) and (len(listaZumbisDireita)==0) and (len(listaZumbisEsquerda)==0) and (len(listaFireDemons)==0):
                    timerFimDaFase += janela.delta_time()
               if timerFimDaFase > 0.5:
                    faseAcabou = True
                    playerMovimentar = False
               if faseAcabou == True:
                    playerMovendoDireita = True
               if (faseAcabou == True) and (player.x > janela.width):
                    modulo = 3
                    vidasPlayer += 1
                    janela.clear()
          
          if playerIntangivel == True:
               timerIntangivel += janela.delta_time()
               timerPiscando += janela.delta_time()
               if timerPiscando > 0.01:
                    playerPiscar *= -1
                    timerPiscando = 0
               if timerIntangivel > 2:
                    playerIntangivel = False
                    timerIntangivel = 0

          if (playerPiscar == 1) or (playerIntangivel == False):
               player.draw()
          janela.draw_text("Vidas: " + str(vidasPlayer), 10, janela.height - 70, 30, (255, 0, 0), "Arial", True, False)
          player.update()
          janela.update()
          fps.tick(60)

          if vidasPlayer <= 0:
               modulo = 1
     
     return modulo, vidasPlayer