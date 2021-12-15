from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

janela = Window(1440, 835)
janela.set_title("Hell World")

cenario = Sprite("cenario.jpg", 1)
chao = Sprite("chao.jpg", 1)
chao.y = cenario.height
jogar = Sprite("botao_jogar.jpg", 1)
dificuldade = Sprite("botao_dificuldade.jpg", 1)
sair = Sprite("botao_sair.jpg", 1)
player = Sprite("soldiergirl.png", 1)
zumbi = Sprite("zumbis.png", 1)

teclado = Window.get_keyboard()
mouse = Window.get_mouse()

mouse.set_position(janela.width/2, janela.height/2)
jogar.x = janela.width/2 - jogar.width/2
dificuldade.x = janela.width/2 - dificuldade.width/2
sair.x = janela.width/2 - sair.width/2
jogar.y = janela.height/2 - jogar.height/2
dificuldade.y = jogar.y + 100 + jogar.height/2 - dificuldade.height/2
sair.y = dificuldade.y + 100 + dificuldade.height/2 - sair.height/2

etapa_menu = 1

while True:
    if teclado.key_pressed("ESC"):
        etapa_menu = 1

    if etapa_menu == 1:
        jogar = Sprite("botao_jogar.jpg", 1)
        dificuldade = Sprite("botao_dificuldade.jpg", 1)
        ranking = Sprite("botao_ranking.jpg", 1)
        sair = Sprite("botao_sair.jpg", 1)
        jogar.x = janela.width/2 - jogar.width/2
        dificuldade.x = janela.width/2 - dificuldade.width/2
        sair.x = janela.width/2 - sair.width/2
        jogar.y = janela.height/2 - jogar.height/2
        dificuldade.y = jogar.y + 100 + jogar.height/2 - dificuldade.height/2
        sair.y = dificuldade.y + 100 + dificuldade.height/2 - sair.height/2

        if mouse.is_over_area((jogar.x, jogar.y),(jogar.x + jogar.width, jogar.y + jogar.height)):
            if mouse.is_button_pressed(1):
                etapa_menu = 2
        elif mouse.is_over_area((dificuldade.x, dificuldade.y),(dificuldade.x + dificuldade.width, dificuldade.y + dificuldade.height)):
            if mouse.is_button_pressed(1):
                etapa_menu = 3
        elif mouse.is_over_area((sair.x, sair.y),(sair.x + sair.width, sair.y + sair.height)):
            if mouse.is_button_pressed(1):
                janela.close()
    
    if etapa_menu == 2:
        cenario = Sprite("cenario.jpg", 1)
        chao = Sprite("chao.jpg", 1)
        player = Sprite("soldiergirl.png", 1)
        zumbi = Sprite("zumbis.png", 1)
        chao.y = cenario.height
        player.x = 100
        player.y = chao.y - player.height
        zumbi.x = chao.width - 300
        zumbi.y = chao.y - zumbi.height

    if etapa_menu == 3:
        facil = Sprite("botao_facil.jpg", 1)
        medio = Sprite("botao_medio.jpg", 1)
        dificil = Sprite("botao_dificil.jpg", 1)
        facil.x = janela.width/3 - facil.width/2
        medio.x = janela.width/3 - medio.width/2
        dificil.x = janela.width/3 - dificil.width/2
        facil.y = jogar.y - facil.height/2
        medio.y = facil.y + 100 + facil.height/2 - medio.height/2
        dificil.y = medio.y + 100 + medio.height/2 - dificil.height/2
        if mouse.is_over_area((facil.x, facil.y),(facil.x + facil.width, facil.y + facil.height)):
            if mouse.is_button_pressed(1):
                etapa_menu = 1
        elif mouse.is_over_area((medio.x, medio.y),(medio.x + medio.width, medio.y + medio.height)):
            if mouse.is_button_pressed(1):
                etapa_menu = 1
        elif mouse.is_over_area((dificil.x, ranking.y),(dificil.x + dificil.width, dificil.y + dificil.height)):
            if mouse.is_button_pressed(1):
                etapa_menu = 1

    if etapa_menu == 1:
        janela.draw_text("Hell World", janela.width/2 - 50, jogar.y + 200, 100, (255, 0, 0), "Arial", True, False)
        jogar.draw()
        dificuldade.draw()
        ranking.draw()
        sair.draw()
    if etapa_menu == 2:
        cenario.draw()
        chao.draw()
        player.draw()
        zumbi.draw()
    if etapa_menu == 3:
        facil.draw()
        medio.draw()
        dificil.draw()
    janela.update()