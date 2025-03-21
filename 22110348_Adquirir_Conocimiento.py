# Chatbot con adquisición de conocimiento mejorado

import time  # Importamos la librería time para añadir pausas en la ejecución

# Base de conocimiento inicial con respuestas predefinidas
base_conocimiento = {
    "hola": "¡Hola! ¿Cómo puedo ayudarte?",
    "como estas": "Estoy bien, gracias por preguntar. ¿Y tú?",
    "bien tambien, me puedes dar informacion sobre un tema": "Cuéntame sobre un tema y aprenderé para responderte después."
}

# Función para obtener una respuesta del chatbot
def obtener_respuesta(mensaje):
    mensaje = mensaje.lower().strip()  # Convertimos a minúsculas y eliminamos espacios extra
    return base_conocimiento.get(mensaje, "No sé la respuesta. ¿Podrías explicármelo?")  # Retornamos la respuesta si existe o pedimos explicación

# Función para aprender nuevas respuestas del usuario
def aprender_respuesta(pregunta, respuesta):
    base_conocimiento[pregunta.lower().strip()] = respuesta.strip()  # Almacena la nueva respuesta en la base de conocimiento
    print("Chatbot: ¡Gracias! Ahora sé responder a esa pregunta.")
    time.sleep(1)  # Pausa breve para una mejor interacción

# Función principal del chatbot
def chat():
    print("Chatbot: ¡Hola! Pregúntame algo o enséñame nuevas cosas. Escribe 'salir' para terminar.")
    while True:
        entrada = input("Tú: ").strip()  # Recibe la entrada del usuario y elimina espacios extra
        if entrada.lower() == "salir":  # Si el usuario escribe 'salir', finaliza el chat
            print("Chatbot: ¡Hasta luego!")
            break
        
        respuesta = obtener_respuesta(entrada)  # Obtiene la respuesta correspondiente
        print("Chatbot:", respuesta)  # Muestra la respuesta del chatbot
        
        if respuesta == "No sé la respuesta. ¿Podrías explicármelo?":  # Si no conoce la respuesta, pide una explicación
            nueva_respuesta = input("Tú (explicación): ").strip()
            if nueva_respuesta:  # Si el usuario proporciona una respuesta, el chatbot la aprende
                aprender_respuesta(entrada, nueva_respuesta)
            else:
                print("Chatbot: No aprendí nada nuevo. Intenta nuevamente.")  # Si la respuesta es vacía, no se guarda

# Ejecutar el chatbot
if __name__ == "__main__":
    chat()  # Inicia la conversación con el chatbot
