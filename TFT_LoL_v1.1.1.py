#
# Script diseñado por Berlineth
#
# +---------------------¡¡IMPORTANTE!!-------------------------+
# |                                                            |
# | Se requiere instalar PyAutoGUI haciendo uso de pip install |
# |                 en la barra de CMD                         |
# |                                                            |
# |       comando para cmd:      pip install PyAutoGUI         |
# |                                                            |
# |                                                            |
# | Se puede hacer caso omiso si se instalo PyAutoGUI          |
# |                                                            |
# +------------------------------------------------------------+
#
# Este es un mini bot que juega por su cuenta TFT de LoL
# Scrip aun en version BETA
#

import datetime, os, time
import pyautogui as pygu

opt = 1
ost = 5
cui = 0
cos = 0
while opt != 0:
    pygu.moveTo(860, 920, .2)
    pygu.mouseDown()
    pygu.mouseUp()  # inicia la partida / compra 1 campeon
    pygu.moveTo(860, 760, .2)
    pygu.mouseDown()
    pygu.mouseUp()  # acepta el inicio de la partida / agarra un campeon
    pygu.moveTo(860, 550, .2)
    pygu.mouseDown()
    pygu.mouseUp()  # suelta el campeon / sale de la partida en caso de perder
    pygu.mouseDown(button='right')
    pygu.mouseUp(button='right')  # se mueve para seleccionar campeon en rotacion
    pygu.moveTo(1525, 160)
    pygu.mouseDown()
    pygu.mouseUp()  # en caso de estar en el menu de tft, cierra cualquier ventana emergente dentro del juego
    pygu.moveTo(320, 115)
    pygu.mouseDown()
    pygu.mouseUp()  # en regresa al grupo para evitar algun bug
    time.sleep(4.25)  # pequeño break para poder detener el programa de forma manual (aun trabajando para que sea automatico)

    cui = cui + 1
    ost = ost - 1
    cos = cos + 1

    if cui == 20:
        pygu.moveTo(1735, 185)
        pygu.mouseDown()
        pygu.mouseUp()
        cui = 0  # cada 20 ciclos cerrara la cola ya que muchas veces puede que ya no entrara a partida y se quede bugeado

    if ost == 1:
        pygu.moveTo(1000, 900, .2)
        pygu.mouseDown()
        pygu.mouseUp()
        ost = 5  # cada 5 ciclos, usa el click para cerrar cualquier ventana de "desafio completado"

    if cos == 3:
        pygu.moveTo(830, 585, .2)
        pygu.mouseDown()
        pygu.mouseUp()
        cos = 0

    tiempo = datetime.datetime.now()
    if tiempo.hour == 8:
        os.system("shutdown /s")  # cambiar el numero de tiempo.hour == () para apagado automatico de la compu
                                  # usando formato horario de 24hr; ejemplo: 5 = 5 am - 20 = 8pm
                                  # ya esta configurado para apagarse automaticamente a las 5 am
