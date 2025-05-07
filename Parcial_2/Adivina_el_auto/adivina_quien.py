import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw
import os

# ---------------------------
# Base de Datos y Atributos
# ---------------------------
atributos = {
    "marca":    [],  # se llena dinámicamente con marcas únicas encontradas en los datos
    "energia":   ["Gasolina", "Diesel", "Eléctrico", "Híbrido"],
    "carroceria":["Sedán", "SUV", "Pickup", "Deportivo", "Hatchback", "Coupé"],
    "puertas":   [2, 4, 5],
    "lujo":      ["Sí", "No"],
    "traccion":  ["Simple", "4x4"],
    "pais":      ["Japón", "Alemania", "Estados Unidos", "Corea del Sur", "Francia"],
    "uso":       ["Urbano", "Familiar", "Deportivo", "Off-Road"],
}

datos_autos = [
    # Toyota
    ["Corolla", "Toyota", 0, 0, 4, 1, 0, 0, "Japón", 0, "toyota_corolla.jpg"],
    ["Camry", "Toyota", 0, 0, 4, 1, 0, 0, "Japón", 0, "toyota_camry.jpg"],
    ["Hilux", "Toyota", 1, 2, 4, 0, 1, 1, "Japón", 1, "toyota_hilux.jpg"],
    ["Land Cruiser", "Toyota", 0, 2, 5, 1, 1, 1, "Japón", 1, "toyota_land_cruiser.jpg"],
    ["RAV4", "Toyota", 3, 2, 5, 1, 1, 0, "Japón", 0, "toyota_rav4.jpg"],
    ["Yaris", "Toyota", 0, 4, 4, 0, 0, 0, "Japón", 0, "toyota_yaris.jpg"],
    ["Tundra", "Toyota", 0, 2, 4, 1, 1, 1, "Japón", 1, "toyota_tundra.jpg"],
    ["Avalon", "Toyota", 0, 0, 4, 1, 0, 0, "Japón", 0, "toyota_avalon.jpg"],
    ["4Runner", "Toyota", 0, 2, 5, 1, 1, 1, "Japón", 1, "toyota_4runner.jpg"],
    ["Prius", "Toyota", 3, 0, 4, 0, 0, 0, "Japón", 0, "toyota_prius.jpg"],

    # BMW
    ["Series 3", "BMW", 0, 0, 4, 1, 0, 0, "Alemania", 0, "bmw_series_3.jpg"],
    ["X5", "BMW", 1, 2, 5, 1, 1, 0, "Alemania", 1, "bmw_x5.jpg"],
    ["M3", "BMW", 0, 0, 2, 1, 0, 0, "Alemania", 0, "bmw_m3.jpg"],
    ["i3", "BMW", 2, 4, 4, 1, 0, 0, "Alemania", 0, "bmw_i3.jpg"],
    ["X3", "BMW", 0, 2, 5, 1, 1, 0, "Alemania", 0, "bmw_x3.jpg"],
    ["Z4", "BMW", 0, 0, 2, 1, 0, 0, "Alemania", 0, "bmw_z4.jpg"],
    ["Series 5", "BMW", 0, 0, 4, 1, 0, 0, "Alemania", 0, "bmw_series_5.jpg"],
    ["X6", "BMW", 0, 2, 5, 1, 1, 0, "Alemania", 0, "bmw_x6.jpg"],
    ["i8", "BMW", 3, 0, 2, 1, 1, 0, "Alemania", 0, "bmw_i8.jpg"],
    ["M4", "BMW", 0, 0, 2, 1, 0, 0, "Alemania", 0, "bmw_m4.jpg"],

    # Ford
    ["F-150", "Ford", 0, 2, 4, 0, 1, 1, "Estados Unidos", 1, "ford_f150.jpg"],
    ["Mustang", "Ford", 0, 0, 2, 1, 0, 0, "Estados Unidos", 0, "ford_mustang.jpg"],
    ["Escape", "Ford", 0, 2, 5, 1, 1, 0, "Estados Unidos", 0, "ford_escape.jpg"],
    ["Explorer", "Ford", 0, 2, 5, 1, 1, 0, "Estados Unidos", 0, "ford_explorer.jpg"],
    ["Focus", "Ford", 0, 0, 4, 0, 0, 0, "Estados Unidos", 0, "ford_focus.jpg"],
    ["Fusion", "Ford", 0, 0, 4, 1, 0, 0, "Estados Unidos", 0, "ford_fusion.jpg"],
    ["Edge", "Ford", 0, 2, 5, 1, 1, 0, "Estados Unidos", 0, "ford_edge.jpg"],
    ["Ranger", "Ford", 1, 2, 4, 0, 1, 1, "Estados Unidos", 1, "ford_ranger.jpg"],
    ["Expedition", "Ford", 0, 2, 5, 1, 1, 1, "Estados Unidos", 1, "ford_expedition.jpg"],
    ["EcoSport", "Ford", 0, 2, 5, 0, 0, 0, "Estados Unidos", 0, "ford_ecosport.jpg"],

    # Honda
    ["Civic", "Honda", 0, 0, 4, 1, 0, 0, "Japón", 0, "honda_civic.jpg"],
    ["Accord", "Honda", 0, 0, 4, 1, 0, 0, "Japón", 0, "honda_accord.jpg"],
    ["CR-V", "Honda", 0, 2, 5, 1, 1, 0, "Japón", 0, "honda_crv.jpg"],
    ["Pilot", "Honda", 0, 2, 5, 1, 1, 1, "Japón", 1, "honda_pilot.jpg"],
    ["HR-V", "Honda", 0, 2, 5, 0, 0, 0, "Japón", 0, "honda_hrv.jpg"],
    ["Ridgeline", "Honda", 1, 2, 4, 0, 1, 1, "Japón", 1, "honda_ridgeline.jpg"],
    ["Fit", "Honda", 0, 0, 4, 0, 0, 0, "Japón", 0, "honda_fit.jpg"], 
    ["Insight", "Honda", 2, 4, 4, 1, 0, 0, "Japón", 0, "honda_insight.jpg"],
    ["Odyssey", "Honda", 0, 2, 5, 1, 1, 0, "Japón", 1, "honda_odyssey.jpg"],
    ["S2000", "Honda", 0, 0, 2, 1, 0, 0, "Japón", 0, "honda_s2000.jpg"],

    # Mercedes-Benz
    ["Clase E", "Mercedes-Benz", 0, 0, 4, 1, 0, 0, "Alemania", 0, "mercedes_clase_e.jpg"],
    ["Clase S", "Mercedes-Benz", 0, 0, 4, 1, 0, 0, "Alemania", 0, "mercedes_clase_s.jpg"],
    ["GLC", "Mercedes-Benz", 0, 2, 5, 1, 1, 0, "Alemania", 0, "mercedes_glc.jpg"],
    ["CLA", "Mercedes-Benz", 0, 0, 4, 1, 0, 0, "Alemania", 0, "mercedes_cla.jpg"],
    ["G-Class", "Mercedes-Benz", 0, 2, 5, 1, 1, 1, "Alemania", 1, "mercedes_gclass.jpg"],
    ["AMG GT", "Mercedes-Benz", 0, 0, 2, 1, 1, 0, "Alemania", 0, "mercedes_amg_gt.jpg"],
    ["A-Class", "Mercedes-Benz", 0, 0, 4, 0, 0, 0, "Alemania", 0, "mercedes_a_class.jpg"],
    ["B-Class", "Mercedes-Benz", 0, 0, 4, 0, 0, 0, "Alemania", 0, "mercedes_b_class.jpg"],
    ["GLE", "Mercedes-Benz", 0, 2, 5, 1, 1, 0, "Alemania", 0, "mercedes_gle.jpg"],
    ["EQC", "Mercedes-Benz", 2, 4, 5, 1, 0, 0, "Alemania", 0, "mercedes_eqc.jpg"],

    # Audi
    ["A4", "Audi", 0, 0, 4, 1, 0, 0, "Alemania", 0, "audi_a4.jpg"],
    ["Q5", "Audi", 0, 2, 5, 1, 1, 0, "Alemania", 0, "audi_q5.jpg"],
    ["Q7", "Audi", 0, 2, 5, 1, 1, 0, "Alemania", 0, "audi_q7.jpg"],
    ["A6", "Audi", 0, 0, 4, 1, 0, 0, "Alemania", 0, "audi_a6.jpg"],
    ["A3", "Audi", 0, 0, 4, 0, 0, 0, "Alemania", 0, "audi_a3.jpg"],
    ["A5", "Audi", 0, 0, 2, 1, 0, 0, "Alemania", 0, "audi_a5.jpg"],
    ["Q3", "Audi", 0, 2, 5, 1, 1, 0, "Alemania", 0, "audi_q3.jpg"],
    ["RS5", "Audi", 0, 0, 2, 1, 0, 0, "Alemania", 0, "audi_rs5.jpg"],
    ["E-Tron", "Audi", 2, 4, 5, 1, 0, 0, "Alemania", 0, "audi_etron.jpg"],
    ["S5", "Audi", 0, 0, 2, 1, 0, 0, "Alemania", 0, "audi_s5.jpg"],
]

# Reconstrucción al formato dict y normalización de los datos
autos = []
for d in datos_autos:
    marca      = d[1].lower()
    energia    = atributos['energia'][d[2]].lower()
    carroceria = atributos['carroceria'][d[3]].lower()
    puertas    = d[4]
    lujo       = atributos['lujo'][d[5]] == "Sí"
    traccion   = atributos['traccion'][d[6]].lower()
    pais       = d[8].lower()
    uso        = atributos['uso'][d[9]].lower()
    imagen     = os.path.join(os.path.dirname(__file__), d[10])  # ruta de imagen
    autos.append({
        'marca': marca,
        'modelo': d[0].lower(),
        'energia': energia,
        'carroceria': carroceria,
        'puertas': puertas,
        'lujo': lujo,
        'traccion': traccion,
        'pais': pais,
        'uso': uso,
        'imagen': imagen
    })
    if marca not in atributos['marca']:
        atributos['marca'].append(marca)

# Estado del juego
autos_filtrados = autos.copy()  # lista filtrada de autos según respuestas
asked = set()                   # atributos ya preguntados
respuestas = []                 # historial de respuestas (atributo, valor, si/no)
current_question = None         # pregunta actual

# ---------------------------
# Motor de Inferencia
# ---------------------------
def generar_posibles_preguntas():
    opciones = []
    total = len(autos_filtrados)
    for attr in ['marca','energia','carroceria','puertas','lujo','traccion','pais','uso']:
        valores = set(a[attr] for a in autos_filtrados)  # valores únicos de este atributo
        for v in valores:
            if (attr, v) in asked:  # ya fue preguntado
                continue
            count = sum(1 for a in autos_filtrados if a[attr] == v)
            if 0 < count < total:  # pregunta útil si no elimina todos ni deja todos
                score = abs(count - total/2)  # mide qué tan balanceada es la división
                opciones.append((attr, v, score))
    return opciones

def seleccionar_pregunta():
    opciones = generar_posibles_preguntas()
    if not opciones:
        return None
    attr, val, _ = min(opciones, key=lambda x: x[2])  # selecciona la mejor pregunta (más informativa)
    
    # Genera el texto de la pregunta
    if attr == 'marca':
        texto = f"¿El auto es de la marca {val.title()}?"
    elif attr == 'energia':
        texto = f"¿El auto funciona con {val}?"
    elif attr == 'carroceria':
        texto = f"¿El auto es un {val}?"
    elif attr == 'puertas':
        texto = f"¿El auto tiene {val} puertas?"
    elif attr == 'lujo':
        texto = "¿El auto es de lujo?" if val else "¿El auto no es de lujo?"
    elif attr == 'traccion':
        texto = f"¿El auto tiene tracción {val}?"
    elif attr == 'pais':
        texto = f"¿El auto es de origen {val.title()}?"
    elif attr == 'uso':
        texto = f"¿El auto se usa para {val}?"
    else:
        texto = f"¿{attr} == {val}?"
    return (attr, val, texto)

# ---------------------------
# Funciones del Juego
# ---------------------------

# Carga una imagen desde el disco y la redimensiona
def cargar_imagen(ruta, size=(100,100)):
    try:
        img = Image.open(ruta)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception:
        # Imagen no encontrada o inválida: muestra un "No Img"
        placeholder = Image.new('RGB', size, color='gray')
        draw = ImageDraw.Draw(placeholder)
        draw.text((10, size[1]//2 - 10), "No Img", fill="white")
        return ImageTk.PhotoImage(placeholder)

# Actualiza la galería de autos mostrados en pantalla
def actualizar_galeria():
    for w in frame_autos.winfo_children():
        w.destroy()
    for auto in autos_filtrados:
        img = cargar_imagen(auto['imagen'])
        lbl = tk.Label(frame_autos, image=img)
        lbl.image = img
        lbl.pack(side='left', padx=5, pady=5)

# Si no hay más preguntas útiles, intenta adivinar por coincidencias
def fallback_guess():
    scores = []
    for a in autos:
        match = 0
        for attr, val, resp in respuestas:
            if resp == 'si' and a[attr] == val:
                match += 1
            if resp == 'no' and a[attr] != val:
                match += 1
        scores.append((match, a))
    return max(scores, key=lambda x: x[0])[1]  # auto con más coincidencias

# Realiza una nueva pregunta al usuario
def hacer_pregunta():
    global current_question
    if len(autos_filtrados) == 1:
        a = autos_filtrados[0]
        messagebox.showinfo("¡Auto encontrado!",
                            f"Tu auto es: {a['marca'].title()} {a['modelo'].title()}")
        root.destroy()
        return
    pq = seleccionar_pregunta()
    if not pq:
        mejor = fallback_guess()
        messagebox.showinfo("¿Será este?",
                            f"Creo que es: {mejor['marca'].title()} {mejor['modelo'].title()}")
        root.destroy()
        return
    current_question = pq
    lbl_pregunta.config(text=pq[2])

# Procesa la respuesta del usuario (sí o no)
def responder(valor):
    global autos_filtrados
    attr, esperado, _ = current_question
    asked.add((attr, esperado))  # marca como preguntado
    respuestas.append((attr, esperado, valor))  # guarda la respuesta

    # Filtra la lista según la respuesta
    if valor.lower() == 'si':
        autos_filtrados = [a for a in autos_filtrados if a[attr] == esperado]
    else:
        autos_filtrados = [a for a in autos_filtrados if a[attr] != esperado]
    
    actualizar_galeria()
    hacer_pregunta()

# ---------------------------
# Interfaz Gráfica
# ---------------------------
root = tk.Tk()
root.title("Adivina el Auto - Juego de Expertos")
root.geometry("900x600")

# Título principal
lbl_titulo = tk.Label(root, text="¿En qué auto estás pensando?", font=("Arial", 20))
lbl_titulo.pack(pady=10)

# Contenedor de imágenes de autos
frame_autos = tk.Frame(root)
frame_autos.pack(fill='x')

# Pregunta actual
lbl_pregunta = tk.Label(root, text="", font=("Arial", 16))
lbl_pregunta.pack(pady=30)

# Botones de respuesta
frame_botones = tk.Frame(root)
frame_botones.pack()
btn_si = tk.Button(frame_botones, text="Sí", width=10, height=2,
                   command=lambda: responder('si'))
btn_si.pack(side='left', padx=20)
btn_no = tk.Button(frame_botones, text="No", width=10, height=2,
                   command=lambda: responder('no'))
btn_no.pack(side='left', padx=20)

# Inicia el juego
actualizar_galeria()
hacer_pregunta()
root.mainloop()
