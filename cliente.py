import requests


API_URL = 'http://127.0.0.1:5000'
token_jwt = None


def registrar_usuario():
    usuario = input('Usuario: ')
    password = input('Password: ')
    resp = requests.post(f'{API_URL}/registro', json={
        'usuario': usuario,
        'password': password
    })
    print(resp.json())

def login_usuario():
    global token_jwt
    usuario = input('Usuario: ')
    password = input('Password: ')
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

def menu():
    while True:
        print('\n1. Registrar usuario')
        print('2. Login')
        print('3. Ver bienvenida')
        print('4. Crear tarea')
        print('5. Salir')
        op = input('Opción: ')
        if op == '1':
            registrar_usuario()
        elif op == '2':
            login_usuario()
        elif op == '3':
            bienvenida()
        elif op == '4':
            crear_tarea()
        elif op == '5':
            break
        else:
            print('Opción inválida')

if __name__ == '__main__':
    menu()
