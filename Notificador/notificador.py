import time
from plyer import notification

if __name__ == '__main__':
    c = 0
    while c<3:
        c += 1
        notification.notify(
            title = 'Has de descansar la vista',
            message = 'hijodeputa',
            timeout = 1 # Temps en segons del notificador
            )
        time.sleep(10) # Temps en [s] entre notificacions
        
