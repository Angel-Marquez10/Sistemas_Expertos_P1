# Función que representa Modus Ponens
def modus_ponens(premisa1, premisa2):
    """
    Aplica la inferencia Modus Ponens:
    Si premisa1 es 'Si P entonces Q' y premisa2 es 'P', concluye 'Q'
    """
    if premisa1 and premisa2:
        return True  # Se cumple la conclusión Q
    return False  # No se puede concluir Q

# Interacción con el usuario
print("¡Bienvenido al sistema de inferencia Modus Ponens!")
print("A continuación, te pediremos que ingreses las premisas para aplicar la regla.")

# Solicitar las premisas
estudió = input("¿La persona estudió? (Sí o No): ").strip().lower()
premisa1 = input("¿La premisa es 'Si estudia, entonces aprobará el examen'? (Sí o No): ").strip().lower()

# Convertir las respuestas en valores booleanos
if estudió == "sí":
    P = True
elif estudió == "no":
    P = False
else:
    print("Respuesta inválida, se asumirá que la persona no estudió.")
    P = False

if premisa1 == "sí":
    P_implica_Q = True
elif premisa1 == "no":
    P_implica_Q = False
else:
    print("Respuesta inválida, se asumirá que la premisa es válida.")
    P_implica_Q = True

# Aplicamos Modus Ponens
resultado = modus_ponens(P_implica_Q, P)

# Mostrar el resultado
if resultado:
    print("\nConclusión: La persona aprobará el examen.")
else:
    print("\nConclusión: No se puede concluir que la persona aprobará el examen.")

