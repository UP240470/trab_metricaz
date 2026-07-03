import os

# (1) Corrección de Vulnerabilidad: Se lee desde el entorno seguro de OS
DB_PASSWORD = os.getenv("DB_PASSWORD")

def calcular_multa(dias_retraso):
    # (2) Corrección de Bug: Se elimina la expresión idéntica redundante del "or"
    if dias_retraso > 30:
        return (dias_retraso - 30) * 10  # Ejemplo: 10 pesos por día de retraso
    return 0

def puede_prestar(socio):
    # (3) Corrección de Code Smell: Se fusionan los dos "if" anidados usando "and"
    if socio.activo and socio.sin_adeudos:
        return True
    return False