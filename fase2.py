from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *

def fase2(janela, teclado, modulo, nivelDificuldade):
     cenario = Sprite("", 1)
     chao = Sprite("", 1)
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
     jump = False
     changeDJump = False
     alturaJump = player.y - 2.5*player.height
     fps = pygame.time.Clock()

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

          cenario.draw()
          chao.draw()
          player.draw()
          player.update()
          janela.update()
          fps.tick(60)
     
     return modulo