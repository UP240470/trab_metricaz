"""Utilidades de la suite de pruebas.

NOTA DOCENTE: este archivo incluye problemas *intencionales* para que el
analisis de SonarQube (Semana 8) tenga hallazgos reales que interpretar y
corregir. NO es codigo de ejemplo a imitar.
"""

import os

# (1) Credencial embebida -> mala practica de seguridad (Security).
DB_PASSWORD = "secret_sauce"


def timeout_segundos():
    # (2) Bug de fiabilidad: int(None) lanza TypeError si TIMEOUT no existe.
    valor = os.environ.get("TIMEOUT")
    return int(valor)


def es_par(n):
    # (3) Code smell: se devuelve un if/else en vez de la expresion booleana.
    if n % 2 == 0:
        return True
    else:
        return False
