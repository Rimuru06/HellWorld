from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

def gameMenu(janela, teclado, mouse, modulo, nivelDificuldade, etapaMenu):
    clickTimer = 0

    while modulo == 1:
        clickTimer += janela.delta_time()
        if teclado.key_pressed("ESC"):
            modulo = 1
            etapaMenu = 1
        janela.set_background_color([0,0,0])
        janela.draw_text("Hell World", janela.width/2 - 180, janela.height/2 - 200, 80, (255, 0, 0), "Arial", True, False)
        if etapaMenu == 1:
            jogar = Sprite("botao_jogar.jpg", 1)
            dificuldade = Sprite("botao_dificuldade.jpg", 1)
            sair = Sprite("botao_sair.jpg", 1)
            jogar.x = janela.width/2 - jogar.width/2
            dificuldade.x = janela.width/2 - dificuldade.width/2
            sair.x = janela.width/2 - sair.width/2
            jogar.y = janela.height/2 - jogar.height/2
            dificuldade.y = jogar.y + 100 + jogar.height/2 - dificuldade.height/2
            sair.y = dificuldade.y + 100 + dificuldade.height/2 - sair.height/2
            if (mouse.is_over_area((jogar.x, jogar.y),(jogar.x + jogar.width, jogar.y + jogar.height))) and (mouse.is_button_pressed(1)) and (clickTimer > 1):
                modulo = 2
                clickTimer = 0
                janela.clear()
            elif (mouse.is_over_area((dificuldade.x, dificuldade.y),(dificuldade.x + dificuldade.width, dificuldade.y + dificuldade.height))) and (mouse.is_button_pressed(1) and (clickTimer > 1)):
                etapaMenu = 2
                clickTimer = 0
                janela.clear()
            elif (mouse.is_over_area((sair.x, sair.y),(sair.x + sair.width, sair.y + sair.height))) and (mouse.is_button_pressed(1) and (clickTimer > 1)):
                janela.close()
            jogar.draw()
            dificuldade.draw()
            sair.draw()
        if etapaMenu == 2:
            facil = Sprite("botao_facil.jpg", 1)
            medio = Sprite("botao_medio.jpg", 1)
            dificil = Sprite("botao_dificil.jpg", 1)
            facil.x = janela.width/2 - facil.width/2
            medio.x = janela.width/2 - medio.width/2
            dificil.x = janela.width/2 - dificil.width/2
            facil.y = janela.height/2 - facil.height/2
            medio.y = facil.y + 100 + facil.height/2 - medio.height/2
            dificil.y = medio.y + 100 + medio.height/2 - dificil.height/2
            if (mouse.is_over_area((facil.x, facil.y),(facil.x + facil.width, facil.y + facil.height))) and (mouse.is_button_pressed(1) and (clickTimer > 1)):
                janela.clear()
                clickTimer = 0
                modulo = 1
                etapaMenu = 1
                nivelDificuldade = 0.5
            elif (mouse.is_over_area((medio.x, medio.y),(medio.x + medio.width, medio.y + medio.height))) and (mouse.is_button_pressed(1) and (clickTimer > 1)):
                janela.clear()
                clickTimer = 0
                modulo = 1
                etapaMenu = 1
                nivelDificuldade = 1
            elif (mouse.is_over_area((dificil.x, sair.y),(dificil.x + dificil.width, dificil.y + dificil.height))) and (mouse.is_button_pressed(1) and (clickTimer > 1)):
                janela.clear()
                clickTimer = 0
                modulo = 1
                etapaMenu = 1
                nivelDificuldade = 3
            facil.draw()
            medio.draw()
            dificil.draw()
        janela.update()

    return modulo, nivelDificuldade, etapaMenu