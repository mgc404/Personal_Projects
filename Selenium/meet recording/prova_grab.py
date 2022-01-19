from pynput import mouse, keyboard
from time import sleep

sleep(5)
ratoli = mouse.Controller()
# Vaig al buscador de windows
ratoli.position = (135, 842)
ratoli.click(mouse.Button.left, 1)
sleep(0.5)
# Busco el programa de grabacio
teclat = keyboard.Controller()
sleep(0.1)
teclat.type('xbox game bar')
sleep(0.2)
teclat.press(keyboard.Key.enter)
# Començo la grabacio
ratoli.position = (240, 108)
sleep(0.5)
ratoli.click(mouse.Button.left, 1)
