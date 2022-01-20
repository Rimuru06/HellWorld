from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *

def inGame(janela, teclado, mouse, modulo, nivelDificuldade):
     cenario = Sprite("cenario.jpg", 1)
     chao = Sprite("chao.jpg", 1)
     chao.y = cenario.height
     player = Animation("player_idle.png", 4, True)
     player.set_sequence_time(0, 3, 240)
     zumbi = Sprite("zumbis.png", 1)
     chao.y = cenario.height
     player.x = 100
     player.y = chao.y - player.height
     playerx = 0
     playery = 0
     ativo = 0
     olhando = 1
     apertou = False
     tempo = 0
     velPlayer = 200
     jump = False
     changeDJump = False
     alturaJump = player.y - 2.5*player.height
     fps = pygame.time.Clock()

     while modulo == 2:
          tempo += janela.delta_time()
          if tempo >= 0.6 and not apertou:
               tempo = 0
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
                    player = Animation("player_run2.png", 12, True)
                    player.set_sequence_time(0, 9, 90)
                    player.x = playerx
                    player.y = playery
                    ativo = 2

          if (teclado.key_pressed("SPACE")) and (jump == False):
               apertou = True
               jump = True
               changeDJump = False
               alturaJump = player.y - player.height
          if jump == True:
               if changeDJump == False:
                    player.y -= velPlayer*janela.delta_time()
               if changeDJump == True:
                    player.y += velPlayer*janela.delta_time()
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