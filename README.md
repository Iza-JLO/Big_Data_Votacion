# Votación con Flask y Redis

Aplicación sencilla para registrar votos y consultar el ranking actual usando Redis como almacenamiento temporal.

## Descripción

La app permite:

- registrar un voto con una matrícula y una opción (`java` o `python`)
- evitar que la misma matrícula vote dos veces
- consultar el ranking actual y quién va ganando
- arrancar una demo automática para probar el flujo completo
- abrir una interfaz mínima desde el navegador para votar y consultar resultados

## Requisitos

- Python 3.10+
- Redis ejecutándose en `localhost:6379`
- acceso a la carpeta del proyecto

## Instalación

1. Clona o descarga el proyecto.
2. Abre la terminal en la raíz del proyecto.
3. Crea un entorno virtual:

```bash
python -m venv .venv
```

4. Activa el entorno virtual:

En PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En bash/zsh:

```bash
source .venv/bin/activate
```

5. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Arrancar el proyecto

Antes de iniciar la app, asegúrate de que Redis esté corriendo en `localhost:6379`.

### Modo normal

```bash
python main.py
```

La aplicación queda disponible en:

```text
http://127.0.0.1:5001/
```

### Modo con demo automática

```bash
python main.py --demo
```

Esto lanza el servidor y ejecuta la demo del cliente para enviar votos de prueba y mostrar el ranking final.

## Endpoints

### Votar

- Método: `POST`
- Ruta: `/votacion/votar`

Ejemplo de cuerpo JSON:

```json
{
  "matricula": "A001",
  "opcion": "java"
}
```

### Resultados

- Método: `GET`
- Ruta: `/resultados`

Ejemplo de respuesta:

```json
{
  "resultados": [
    {"opcion": "python", "votos": 2},
    {"opcion": "java", "votos": 1}
  ],
  "ganando": "python"
}
```

## Interfaz web

La ruta `/` sirve una página mínima desde Flask con un formulario para votar y un botón para consultar resultados desde el navegador.

## Reiniciar el estado

Si quieres borrar los votos guardados en Redis durante pruebas, puedes ejecutar:

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
r.delete('votos', 'votantes')
```

Para limpiar todo Redis:

```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
r.flushall()
```

## Estructura principal

```text
.
├── main.py
├── cliente.py
├── servidor.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── .gitignore
```

## Nota

El proyecto está pensado para una prueba simple y didáctica de Flask + Redis. Por eso la lógica se mantiene mínima y clara, con una demo para verificar el flujo completo sin sobrecomplicar la implementación.