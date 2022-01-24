from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *

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
     velPlayer = 200
     velTiro = 800
     jump = False
     changeDJump = False
     alturaJump = player.y - 2.5*player.height
     fps = pygame.time.Clock()
     projeteisPlayerFrente = []
     projeteisPlayerTras = []
     playerVoltadoPraFrente = True
     timerTiro = 0
     playerAtirou = False

     while modulo == 2:
          tempoTrocaSprite += janela.delta_time()
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
          if teclado.key_pressed("ESC"):
               modulo = 1
          if teclado.key_pressed("RIGHT"):
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
                    tiroPlayer.y = player.y + 10
                    tiroPlayer.x = player.x + player.width
                    projeteisPlayerFrente.append(tiroPlayer)
                    print("DEVIA ESTAR ATIRANDO PRA FRENTE")
               elif playerVoltadoPraFrente == False:
                    tiroPlayer = Sprite("tiroPlayer.png", 1)
                    tiroPlayer.y = player.y + 10
                    tiroPlayer.x = player.x
                    projeteisPlayerTras.append(tiroPlayer)
                    print("DEVIA ESTAR ATIRANDO PRA TRÁS")
          
          if playerAtirou == True:
               timerTiro += janela.delta_time()
               if timerTiro > 0.2:
                    playerAtirou = False
                    timerTiro = 0
          
          for t in range(len(projeteisPlayerFrente)-1, -1, -1):
               projeteisPlayerFrente[t].x += velTiro*janela.delta_time()
               projeteisPlayerFrente[t].draw()
          
          for t in range(len(projeteisPlayerTras)-1, -1, -1):
               projeteisPlayerTras[t].x -= velTiro*janela.delta_time()
               projeteisPlayerTras[t].draw()

          cenario.draw()
          chao.draw()
          player.draw()
          player.update()
          janela.update()
          fps.tick(60)
     
     return modulo