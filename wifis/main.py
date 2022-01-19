import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if 'Perfil de todos los usuarios' in line]
print(wifis)

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if 'Contenido de la clave' in line]
    try:
        print(f'Name: {wifi}, Password: {results[0]}')
    except IndexError:
        print(f'Name: {wifi}, Password: Empty')
        

