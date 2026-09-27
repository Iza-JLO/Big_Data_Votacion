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

@app.route("/votacion/votar", methods=["POST"])
def votar():
    return "xd"