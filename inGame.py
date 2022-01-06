from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def inGame(janela, teclado, mouse, modulo, nivelDificuldade):
     cenario = Sprite("cenario.jpg", 1)
     chao = Sprite("chao.jpg", 1)
     chao.y = cenario.height
     player = Sprite("soldiergirl.png", 1)
     zumbi = Sprite("zumbis.png", 1)
     chao.y = cenario.height
     player.x = 100
     player.y = chao.y - player.height
     velPlayer = 200
     jump = False
     changeDJump = False
     alturaJump = player.y - 1.5*player.height

     while modulo == 2:
          if teclado.key_pressed("ESC"):
               modulo = 1
          if teclado.key_pressed("RIGHT"):
               player.x += velPlayer*janela.delta_time()
          elif teclado.key_pressed("LEFT"):
               player.x -= velPlayer*janela.delta_time()
          if (teclado.key_pressed("SPACE")) and (jump == False):
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
          elif player.y >= chao.y - 1.5*player.height:
               jump = False
          cenario.draw()
          chao.draw()
          player.draw()
          janela.update()
     
     return modulo