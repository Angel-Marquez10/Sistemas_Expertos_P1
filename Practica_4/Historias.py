# src/stories.py

# Definición de personajes: (clave, nombre, profesión)
CHARACTERS = {
    'A': ('Dra. Álvarez', 'Médica'),
    'G': ('Capitán Gómez', 'Militar'),
    'R': ('Chef Ramírez', 'Cocinero'),
    'M': ('Profesora Molina', 'Docente'),
    'D': ('Inspector Díaz', 'Policía')
}

# Locaciones: clave y nombre
LOCATIONS = {
    'B': 'Biblioteca',
    'S': 'Salón Principal',
    'C': 'Cocina',
    'Q': 'Cuarto de Estar',
    'T': 'Taller'
}

# Armas: clave y nombre
WEAPONS = {
    'P': 'Puñal antiguo',
    'S': 'Pistola de época',
    'C': 'Cuerda de begonia',
    'L': 'Candelabro de bronce',
    'W': 'Llave inglesa'
}

# Historias finales: {(char, weapon, loc): relato}
STORIES = {
    ('A', 'P', 'B'): (
        "Dra. Álvarez y el puñal en la Biblioteca",
        "La Dra. Álvarez, convencida de que el profesor Soto la estaba traicionando en su investigación médica, asestó el puñal antiguo en medio de la Biblioteca. Su ambición científica la llevó a un trágico desenlace."
    ),
    ('G', 'S', 'S'): (
        "Capitán Gómez y la pistola en el Salón Principal",
        "Al descubrir contrabando en el Salón Principal, el Capitán Gómez perdió la compostura y desenfundó su pistola de época, acabando en un fatídico disparo."
    ),
    ('R', 'C', 'C'): (
        "Chef Ramírez y la cuerda en la Cocina",
        "Celos profesionales tras el robo de una receta secreta hicieron que el Chef Ramírez estrangulara al maestro panadero con la cuerda de begonia en la Cocina."
    ),
    ('M', 'L', 'Q'): (
        "Profesora Molina y el candelabro en el Cuarto de Estar",
        "La Profesora Molina, indignada por acusaciones de plagio, alzó el candelabro de bronce y asestó un golpe mortal en el Cuarto de Estar."
    ),
    ('D', 'W', 'T'): (
        "Inspector Díaz y la llave inglesa en el Taller",
        "Para encubrir pruebas de corrupción policial, el Inspector Díaz atacó al mecánico con la llave inglesa en el Taller, terminando con un destino trágico."
    )
}