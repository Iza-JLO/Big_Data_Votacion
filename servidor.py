from flask import Flask, jsonify, request, render_template
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/votacion/votar', methods=['POST'])
def votar():
    body = request.get_json()
    matricula = body.get('matricula')
    opcion = body.get('opcion')

    if not matricula or not opcion:
        return jsonify({'error': 'Faltan datos (matricula y opcion)'}), 400

    if opcion not in ('java', 'python'):
        return jsonify({'error': 'Opción inválida, debe ser java o python'}), 400

    if r.sismember('votantes', matricula):
        return jsonify({'error': 'Esta matrícula ya votó'}), 409

    r.zincrby('votos', 1, opcion)
    r.sadd('votantes', matricula)

    return jsonify({'ok': True, 'mensaje': f'Voto registrado para {opcion}'})

@app.route('/resultados')
def resultados():
    ranking = r.zrevrange('votos', 0, -1, withscores=True)

    resultados_formateados = [
        {'opcion': opcion, 'votos': int(score)}
        for opcion, score in ranking
    ]

    ganador = resultados_formateados[0]['opcion'] if resultados_formateados else None

    return jsonify({
        'resultados': resultados_formateados,
        'ganando': ganador
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)