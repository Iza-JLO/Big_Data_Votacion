import requests

BASE_URL = 'http://localhost:5001'

def separador(titulo):
    print('\n' + '=' * 50)
    print(titulo)
    print('=' * 50)

def demo_votacion():
    separador('DEMO: Votación Java vs Python')

    votos = [
        ('A001', 'python'),
        ('A002', 'java'),
        ('A003', 'python'),
        ('A001', 'java'),  #matrícula repetida
    ]

    for matricula, opcion in votos:
        resp = requests.post(f'{BASE_URL}/votacion/votar',
                              json={'matricula': matricula, 'opcion': opcion})
        print(f'{matricula} vota {opcion}: {resp.status_code} - {resp.json()}')

    resp = requests.get(f'{BASE_URL}/resultados')
    print('\nResultados actuales:', resp.json())

if __name__ == '__main__':
    demo_votacion()