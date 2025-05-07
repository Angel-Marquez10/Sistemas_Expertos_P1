# autos.py
# Base de datos de autos simplificada con más marcas

# Atributos comunes
atributos = {
    "energia": ["Gasolina", "Diesel", "Eléctrico", "Híbrido"],
    "carroceria": ["Sedán", "SUV", "Pickup", "Deportivo", "Hatchback", "Coupé"],
    "puertas": [2, 4, 5],
    "lujo": ["Sí", "No"],
    "traccion": ["Simple", "4x4"],
    "pais": ["Japón", "Alemania", "Estados Unidos", "Corea del Sur", "Francia"],
    "uso": ["Urbano", "Familiar", "Deportivo", "Off-Road"],
}

# Lista de autos (cada uno con el índice correspondiente a sus características)
autos = [
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

# Función para obtener las características de un auto
def obtener_auto_por_modelo(modelo):
    for auto in autos:
        if auto[0].lower() == modelo.lower():
            return auto
    return None