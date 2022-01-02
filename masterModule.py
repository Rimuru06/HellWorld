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
etapaMenu = 1
clickTimer = 0.0

while True:
    if teclado.key_pressed("ESC"):
        modulo = 1
        etapaMenu = 1
    
    if modulo == 1:
        modulo, nivelDificuldade, etapaMenu = gameMenu(janela, teclado, mouse, modulo, nivelDificuldade, etapaMenu, clickTimer)

    if modulo == 2:
        inGame(janela, teclado, mouse, modulo, nivelDificuldade, clickTimer)

    janela.update()