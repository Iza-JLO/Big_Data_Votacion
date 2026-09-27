import requests

URL = "http://localhost:5000"


matricula = input("Matrícula: ")
voto_opcion = input("¿Java o Python?: ").lower()


#Este es para el endpoint de votacion
respuesta = requests.post(f"{URL}/votacion/votar",
                          json={
                          "matricula": matricula,
                          "opcion": voto_opcion})

#Pa checar:
print(respuesta.json())