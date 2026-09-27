"""
PRACTICA

Harán un servidor con

    Endpoint 1
        Permitir registrar votos y guardarlos en un sorted set de redis
        El servidor recibirá la opción por la que votan y la matricula de quien vota

    No se debe poder registrar un voto si esa matricula ya votó


Endpoint 2
    Poder consultar quien va ganando en todo momento
"""


from flask import Flask, jsonify, request
import redis

app = Flask(__name__)

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

VOTOS = "votos"
MATRICULAS = "matriculas"


#ESTE ES EL PRIMER ENDPOINT: VOTACIONES
@app.route("/votacion/votar", methods=["POST"])
def votar():
    #Datos de entrada desde el json que puse en cliente.py
    datos_entrada = request.get_json()
    matricula = datos_entrada["matricula"]
    opcion = datos_entrada["opcion"]

    if r.sismember(MATRICULAS, matricula): #
        return jsonify({
            "mensaje": "La matricula propocionada ya votó. :p"
        }), 400

    #Cuando la matricula no está registrada en Matriculas:
    r.zincrby(VOTOS, 1, opcion)   #Esto está padre para revisar
    r.sadd(MATRICULAS, matricula) #Este también

    return jsonify({
        "mensaje": "El voto a sido registrado.",
        "opcion": "opcion"
    }), 201



#Este bloque es para que arranque el servidor y no se cierre.
if __name__ == "__main__":
    app.run(debug=True, port=5000)