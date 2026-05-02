import requests
import getpass


API_URL = 'http://127.0.0.1:5000'
token_jwt = None


def registrar_usuario():
    usuario = input('Usuario: ')
    password = getpass.getpass('Password: ')
    resp = requests.post(f'{API_URL}/registro', json={
        'usuario': usuario,
        'password': password
    })
    print(resp.json())

def login_usuario():
    global token_jwt
    usuario = input('Usuario: ')
    password = getpass.getpass('Password: ')
    resp = requests.post(f'{API_URL}/login', json={
        'usuario': usuario,
        'password': password
    })
    data = resp.json()
    print(data)
    if resp.status_code == 200 and 'token' in data:
        token_jwt = data['token']
        print('Token guardado para futuras operaciones protegidas.')
    else:
        token_jwt = None

def bienvenida():
    global token_jwt
    if not token_jwt:
        print('Primero debes hacer login para obtener el token.')
        return
    headers = {'Authorization': f'Bearer {token_jwt}'}
    resp = requests.get(f'{API_URL}/tareas', headers=headers)
    print(resp.text)

def crear_tarea():
    global token_jwt
    if not token_jwt:
        print('Primero debes hacer login para obtener el token.')
        return
    descripcion = input('Descripción de la tarea: ')
    headers = {'Authorization': f'Bearer {token_jwt}'}
    resp = requests.post(f'{API_URL}/tareas', json={
        'descripcion': descripcion
    }, headers=headers)
    try:
        print(resp.json())
    except Exception:
        print(resp.text)

def ver_pendientes():
    global token_jwt
    if not token_jwt:
        print('Primero debes hacer login para obtener el token.')
        return
    headers = {'Authorization': f'Bearer {token_jwt}'}
    resp = requests.get(f'{API_URL}/tareas/pendientes', headers=headers)
    tareas = resp.json()
    if not tareas:
        print('No tenés tareas pendientes.')
    else:
        print('\nTareas pendientes:')
        for t in tareas:
            print(f'  [ID: {t["id"]}] {t["descripcion"]}')

def completar_tarea():
    global token_jwt
    if not token_jwt:
        print('Primero debes hacer login para obtener el token.')
        return
    entrada = input('ID/s de tarea a completar (separados por coma): ')
    ids = [int(x.strip()) for x in entrada.split(',') if x.strip().isdigit()]
    if not ids:
        print('No se ingresaron IDs válidos.')
        return
    headers = {'Authorization': f'Bearer {token_jwt}'}
    if len(ids) == 1:
        resp = requests.patch(f'{API_URL}/tareas/{ids[0]}', headers=headers)
    else:
        resp = requests.patch(f'{API_URL}/tareas/completar', json={'ids': ids}, headers=headers)
    try:
        print(resp.json())
    except Exception:
        print(resp.text)

def menu():
    while True:
        print('\n1. Registrar usuario')
        print('2. Login')
        print('3. Ver todas las tareas')
        print('4. Ver tareas pendientes')
        print('5. Crear tarea')
        print('6. Completar tarea')
        print('7. Salir')
        op = input('Opción: ')
        if op == '1':
            registrar_usuario()
        elif op == '2':
            login_usuario()
        elif op == '3':
            bienvenida()
        elif op == '4':
            ver_pendientes()
        elif op == '5':
            crear_tarea()
        elif op == '6':
            completar_tarea()
        elif op == '7':
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    try:
        menu()
    except KeyboardInterrupt:
        print('\nSaliendo...')
