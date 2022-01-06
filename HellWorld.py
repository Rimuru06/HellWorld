from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from gameMenu import gameMenu
from inGame import inGame

janela = Window(1440, 835)
janela.set_title("Hell World")

teclado = Window.get_keyboard()
mouse = Window.get_mouse()

modulo = 1
nivelDificuldade = 1

while True:
    etapaMenu = 1
    
    if modulo == 1:
        modulo, nivelDificuldade, etapaMenu = gameMenu(janela, teclado, mouse, modulo, nivelDificuldade, etapaMenu)

    if modulo == 2:
        modulo = inGame(janela, teclado, mouse, modulo, nivelDificuldade)

    janela.update()