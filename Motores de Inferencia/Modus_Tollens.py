# Función que representa Modus Tollens
def modus_tollens(premisa1, premisa2):
    """
    Aplica la inferencia Modus Tollens:
    Si premisa1 es 'Si P entonces Q' y premisa2 es 'No Q', concluye 'No P'
    """
    if not premisa2 and premisa1:
        return True  # Se puede concluir que no P
    return False  # No se puede concluir que no P

# Interacción con el usuario
print("¡Bienvenido al sistema de inferencia Modus Tollens!")
print("A continuación, te pediremos que ingreses las premisas para aplicar la regla.")

# Solicitar las premisas
fiebre = input("¿El paciente tiene fiebre? (Sí o No): ").strip().lower()
premisa1 = input("¿La premisa es 'Si tiene fiebre, entonces tiene COVID-19'? (Sí o No): ").strip().lower()

# Convertir las respuestas en valores booleanos
if fiebre == "sí":
    Q = True
elif fiebre == "no":
    Q = False
else:
    print("Respuesta inválida, se asumirá que el paciente no tiene fiebre.")
    Q = False

if premisa1 == "sí":
    P_implica_Q = True
elif premisa1 == "no":
    P_implica_Q = False
else:
    print("Respuesta inválida, se asumirá que la premisa es válida.")
    P_implica_Q = True

# Aplicamos Modus Tollens
resultado = modus_tollens(P_implica_Q, Q)

# Mostrar el resultado
if resultado:
    print("\nConclusión: El paciente no tiene COVID-19.")
else:
    print("\nConclusión: No se puede concluir que el paciente no tiene COVID-19.")
