import tkinter as tk
from tkinter import ttk

# Narrativa resumida para cada paso
FLOW_NODES = {
    "Start": "Inicio",
    "Welcome": "Pantalla Bienvenida\n(COMENZAR AVENTURA)",
    "Init": "Inicializar Juego:\nElegir culpable, arma y ubicación",
    "Chap1": "Capítulo 1:\nDescubrir cuerpo y arma",
    "Chap2": "Capítulo 2:\nHuellas y nota misteriosa",
    "Chap3": "Capítulo 3:\nGrabación de cámara revela sospechoso",
    "Chap4": "Capítulo 4:\nDiario con plan de venganza",
    "Chap5": "Capítulo 5:\nConfrontación final y motivo",
    "Clue": "Mostrar Pista:\nEliminar opción incorrecta",
    "Accuse": "Acusar:\nSeleccionar y comprobar",
    "Result": "Resultado:\nÉxito o Fallo",
    "Restart": "Reiniciar Juego"
}
EDGES = [
    ("Start", "Welcome"), ("Welcome", "Init"),
    ("Init", "Chap1"), ("Chap1", "Chap2"), ("Chap2", "Chap3"),
    ("Chap3", "Chap4"), ("Chap4", "Chap5"), ("Chap5", "Clue"),
    ("Clue", "Accuse"), ("Accuse", "Result"), ("Result", "Restart")
]
# Posiciones X,Y en pixeles
POSITIONS = {
    "Start": (50, 50),
    "Welcome": (300, 50),
    "Init": (550, 50),
    "Chap1": (100, 200),
    "Chap2": (100, 350),
    "Chap3": (100, 500),
    "Chap4": (400, 200),
    "Chap5": (400, 350),
    "Clue": (400, 500),
    "Accuse": (700, 350),
    "Result": (700, 500),
    "Restart": (550, 650)
}

class FlowchartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diagrama de Flujo Completo - Clue")
        # Contenedor con scrollbars
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        # Canvas y scrollbars
        self.canvas = tk.Canvas(container, bg="white", scrollregion=(0,0,900,800))
        hbar = ttk.Scrollbar(container, orient='horizontal', command=self.canvas.xview)
        vbar = ttk.Scrollbar(container, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        hbar.grid(row=1, column=0, sticky='ew')
        vbar.grid(row=0, column=1, sticky='ns')
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        self._draw_flowchart()

    def _draw_flowchart(self):
        # Dibujar nodos
        centers = {}
        for key, text in FLOW_NODES.items():
            x, y = POSITIONS[key]
            cx, cy = self._draw_node(x, y, text)
            centers[key] = (cx, cy)
        # Dibujar flechas
        for a, b in EDGES:
            self._draw_arrow(centers[a], centers[b])

    def _draw_node(self, x, y, text, width=200, height=80):
        # Rectángulo con fondo suave y borde
        rect = self.canvas.create_rectangle(x, y, x+width, y+height,
                                            fill="#E8F4FD", outline="#1A73E8", width=2,
                                            roundness=20 if hasattr(self.canvas, 'roundness') else None)
        # Texto centrado y multilinea
        self.canvas.create_text(x+width/2, y+height/2, text=text,
                                font=("Arial", 10), fill="#1A73E8", width=width-10)
        return (x+width/2, y+height/2)

    def _draw_arrow(self, p1, p2):
        # Línea curva o recta con flecha
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], arrow='last',
                                width=2, fill="#555")

if __name__ == "__main__":
    app = FlowchartApp()
    app.mainloop()
