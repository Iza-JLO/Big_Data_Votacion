"""Punto de entrada del proyecto.

Este archivo no duplica la lógica del servidor; solo lanza la app real
implementada en servidor.py y puede ejecutar la demo del cliente si se
solicita por parámetro.
"""

import argparse
import threading
import time

from cliente import demo_votacion
from servidor import app


def ejecutar_demo():
    """Ejecución en segundo plano para no bloquear el arranque del servidor."""
    time.sleep(1.5)
    demo_votacion()


def main():
    parser = argparse.ArgumentParser(description="Inicia el servidor de votación.")
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Ejecuta la demo del cliente tras arrancar el servidor.",
    )
    args = parser.parse_args()

    if args.demo:
        threading.Thread(target=ejecutar_demo, daemon=True).start()

    app.run(debug=True, port=5001)


if __name__ == "__main__":
    main()