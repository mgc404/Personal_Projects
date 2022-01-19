from time import sleep

from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller
keyboard = Controller()

def preg_y_n(s):
    r = input(s)
    if r == 'n':
        exit()
        
ll_jocs = [['Age of Empires II (2013)',(395, 225), 0],
           ['Call of Duty Modern Warfare 2 - Multiplayer', (395, 250), 1],
           ['Dyson Sphere Program', (395, 275), 1],
           ['Stellaris', (395, 425), 0],
           ['Subnautica', (393, 435), 1]]

ll_users = [['grums0', 'grum1956'],['miquelgarcia11', 'reventaOjetes69']]

for i in range(len(ll_jocs)):
    print(' ' + str(i) + ' ---> ' + ll_jocs[i][0])
    
joc = int(input('Enter the number of the game: '))


print('Minimitzar cmd')
# Minimitzar cmd
keyboard.press(Key.cmd)
keyboard.tap('d')
keyboard.release(Key.cmd)
sleep(1)

# Obre "good stuff"
print('Obre "good stuff"')
mouse.position = (58, 290)
mouse.click(Button.left, 2)
sleep(1.5)
preg_y_n('')
# Maximitza
keyboard.press(Key.home)
keyboard.tap(Key.f11)
keyboard.release(Key.home)
sleep(1)
preg_y_n('')
# Doble click al joc
print('Doble click al joc?')
mouse.position = ll_jocs[joc][1]
##preg_y_n('Es aquest? ({})'.format(ll_jocs[joc][1]))
##mouse.position = ll_jocs[joc][1]
mouse.click(Button.left, 2)
sleep(7)

# User
print('User')
mouse.position = (800, 350)
mouse.click(Button.left, 2)
keyboard.tap(Key.delete)
for car in ll_users[ll_jocs[joc][2]][0]:
    sleep(0.01)
    keyboard.tap(car)
sleep(0.5)
# Contra
print('Contra')
mouse.position = (800, 375)
mouse.click(Button.left, 1)
for car in ll_users[ll_jocs[joc][2]][1]:
    sleep(0.01)
    keyboard.tap(car)
print('enter')
# enter
mouse.position = (750, 440)
sleep(0.5)
mouse.click(Button.left, 1)
exit()
    
