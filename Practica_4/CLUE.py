import tkinter as tk
from tkinter import ttk, messagebox, Menu
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import os

# --- Datos del juego ---
PERSONAJES = [
    {"nombre": "Detective Ana", "profesion": "Detective"},
    {"nombre": "Chef Luis",    "profesion": "Chef"},
    {"nombre": "Doctora Eva",  "profesion": "Médica"},
    {"nombre": "Artista Pablo","profesion": "Artista"},
    {"nombre": "Profesor Rosa","profesion": "Profesor"},
    {"nombre": "Jardinero Leo","profesion": "Jardinero"}
]
UBICACIONES = ["Sala", "Cocina", "Biblioteca", "Jardín", "Dormitorio", "Estudio"]
ARMAS = ["Cuchillo", "Candelabro", "Pistola", "Cuerda", "Tubo", "Veneno"]

ESCENARIO = (
    "Noche lluviosa en la mansión Colomos. Un grito resuena en los pasillos mientras las luces titilan."
)
CHAPTERS = [
    # Capítulo 1
    (
        "Capítulo 1: La sirena policial ilumina la {ubicacion}. "
        "La puerta está entreabierta y dentro, {nombre} descubre un cuerpo junto al {arma} ensangrentado."
    ),
    # Capítulo 2
    (
        "Capítulo 2: El suelo de la {ubicacion} está cubierto de huellas fangosas. "
        "Solo calza el pie de {nombre}."
    ),
    # Capítulo 3
    (
        "Capítulo 3: Revisan la grabación de la cámara de seguridad. "
        "Se ve a {nombre} entrar con prisa y manipular el {arma}."
    ),
    # Capítulo 4
    (
        "Capítulo 4: Encuentran un diario con la letra de {nombre}. "
        "En la página anterior, hay un plan detallado con el {arma}."
    ),
    # Capítulo 5
    (
        "Capítulo 5: Todas las piezas encajan: {nombre}, un/a {profesion}, tenía acceso al {arma} en la {ubicacion}."
    )
]
CLUES = [
    "Se encontró un trozo de tela rojo.",
    "Las huellas llevan hacia la ventana lateral.",
    "El reloj detenido marca las 10:15.",
    "Hay un derrame de tinta junto al diario.",
    "Restos de cera de velas en el pomo."
]
FINALES = [
    "Capturan a {nombre} con el {arma} en la {ubicacion}.",
    "{nombre} huye, pero deja rastro del {arma}.",
    "{nombre} confiesa el crimen con el {arma}.",
    "{nombre} destruye el {arma} y escapa.",
    "Pese a dudas, todo incrimina a {nombre}."
]

class ClueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🔍 Clue Interactivo Mejorado")
        self.geometry("1024x700")
        self.config(bg="#2c3e50")
        self._load_paths()
        self._create_menu()
        self._create_frames()
        self._show_welcome()

    def _load_paths(self):
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.assets = os.path.join(self.base, "assets")

    def _create_menu(self):
        menubar = Menu(self)
        game = Menu(menubar, tearoff=0)
        game.add_command(label="Nueva Partida", command=self._start_game)
        game.add_command(label="Instrucciones", command=self._show_instructions)
        game.add_separator()
        game.add_command(label="Salir", command=self.destroy)
        menubar.add_cascade(label="Juego", menu=game)
        self.config(menu=menubar)

    def _create_frames(self):
        # Welcome frame
        self.welcome_frame = tk.Frame(self, bg="#ecf0f1")
        tk.Label(self.welcome_frame,
                 text="BIENVENIDO A CLUE",
                 bg="#ecf0f1", font=("Arial",24,'bold')).pack(pady=20)
        tk.Label(self.welcome_frame, text=ESCENARIO,
                 bg="#ecf0f1", wraplength=800, justify="left").pack(pady=10)
        # Start button
        self.start_btn = tk.Button(self.welcome_frame, text="COMENZAR AVENTURA",
                                   font=("Arial",16,'bold'), bg="#2980b9", fg="white",
                                   command=self._start_game)
        self.start_btn.pack(pady=30)

        # Game frame
        self.game_frame = tk.Frame(self, bg="#2c3e50")
        sidebar = tk.Frame(self.game_frame, bg="#34495e", width=240)
        sidebar.pack(side="left", fill="y")
        tk.Label(sidebar, text="Capítulos", bg="#34495e", fg="white",
                 font=("Arial",14,'bold')).pack(pady=10)
        self.chapter_buttons = []
        for i in range(5):
            btn = tk.Button(sidebar, text=f"Capítulo {i+1}", state="disabled",
                            width=20, command=lambda idx=i: self._display_chapter(idx))
            btn.pack(pady=2)
            self.chapter_buttons.append(btn)
        self.clue_btn = tk.Button(sidebar, text="Mostrar Pista", state="disabled",
                                  width=20, command=self._show_clue)
        self.clue_btn.pack(pady=10)
        ttk.Separator(sidebar).pack(fill="x", pady=10)
        accuse_frame = tk.LabelFrame(sidebar, text="Acusar al culpable",
                                     bg="#34495e", fg="white", font=("Arial",12,'bold'))
        accuse_frame.pack(pady=10, padx=10, fill="x")
        self.combo_person = ttk.Combobox(accuse_frame, state="disabled")
        self.combo_person.pack(fill="x", padx=5, pady=2)
        self.combo_weapon = ttk.Combobox(accuse_frame, state="disabled")
        self.combo_weapon.pack(fill="x", padx=5, pady=2)
        self.combo_place = ttk.Combobox(accuse_frame, state="disabled")
        self.combo_place.pack(fill="x", padx=5, pady=2)
        self.btn_accuse = tk.Button(accuse_frame, text="¡Acusar!", state="disabled",
                                    command=self._check_accusation)
        self.btn_accuse.pack(pady=10)
        # Restart button
        self.btn_restart = tk.Button(accuse_frame, text="Reiniciar Juego", state="disabled",
                                     command=self._restart_game)
        self.btn_restart.pack(pady=5)

        main = tk.Frame(self.game_frame, bg="#ecf0f1")
        main.pack(side="right", fill="both", expand=True)
        self.game_title = tk.Label(main, text="", bg="#ecf0f1",
                                   font=("Arial",20,'bold'))
        self.game_title.pack(pady=10)
        self.game_text = tk.Text(main, wrap="word", font=("Arial",14),
                                 bd=0, bg="#ecf0f1", height=8)
        self.game_text.pack(padx=20)
        self.image_label = tk.Label(main, bg="#ecf0f1")
        self.image_label.pack(pady=10)

    def _show_welcome(self):
        self.game_frame.pack_forget()
        self.welcome_frame.pack(fill="both", expand=True)

    def _start_game(self):
        # Hide welcome, show game
        self.welcome_frame.pack_forget()
        self.game_frame.pack(fill="both", expand=True)
        # Random solution
        self.solution = {
            'personaje': random.choice(PERSONAJES),
            'arma': random.choice(ARMAS),
            'ubicacion': random.choice(UBICACIONES)
        }
        # Enable UI elements
        for btn in self.chapter_buttons:
            btn.config(state="normal")
        self.clue_btn.config(state="normal")
        self.combo_person.config(values=[p['nombre'] for p in PERSONAJES], state="readonly")
        self.combo_weapon.config(values=ARMAS, state="readonly")
        self.combo_place.config(values=UBICACIONES, state="readonly")
        # Start first chapter
        self._display_chapter(0)

    def _display_chapter(self, idx):
        # Show chapter text
        tpl = CHAPTERS[idx]
        data = {
            'nombre': self.solution['personaje']['nombre'],
            'profesion': self.solution['personaje']['profesion'],
            'arma': self.solution['arma'],
            'ubicacion': self.solution['ubicacion']
        }
        text = tpl.format(**data)
        self.game_title.config(text=f"Capítulo {idx+1}")
        self.game_text.config(state="normal")
        self.game_text.delete("1.0", tk.END)
        self.game_text.insert(tk.END, text)
        self.game_text.config(state="disabled")
        # Load image
        filename = f"chapter{idx+1}.jpg"
        path = os.path.join(self.assets, filename)
        if not os.path.exists(path):
            key = ['ubicacion','personaje','arma','personaje','profesion'][idx]
            val = data[key] if key in data else data['nombre']
            filename = f"{val.replace(' ', '_').lower()}.jpg"
        self._load_image(filename)
        # Enable accuse on last chapter
        if idx == 4:
            self.btn_accuse.config(state="normal")

    def _show_clue(self):
        idx = int(self.game_title.cget("text").split()[-1]) - 1
        pista = CLUES[idx].format(ubicacion=self.solution['ubicacion'])
        messagebox.showinfo("Pista", pista)

    def _load_image(self, filename):
        path = os.path.join(self.assets, filename)
        try:
            img = Image.open(path)
        except:
            img = Image.new("RGB", (400,300), color=(200,200,200))
            d = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            d.text((100,140), "Imagen no disponible", font=font, fill=(50,50,50))
        img = img.resize((400,300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def _check_accusation(self):
        p = self.combo_person.get()
        a = self.combo_weapon.get()
        u = self.combo_place.get()
        if p == self.solution['personaje']['nombre'] and a == self.solution['arma'] and u == self.solution['ubicacion']:
            msg = random.choice(FINALES).format(
                nombre=p, arma=a, ubicacion=u
            )
            messagebox.showinfo("¡Correcto!", msg)
            # Enable restart after correct
            self.btn_restart.config(state="normal")
        else:
            messagebox.showerror("Fallido", "Acusación incorrecta.")

    def _restart_game(self):
        # Reset UI and start new game
        self.btn_restart.config(state="disabled")
        self.btn_accuse.config(state="disabled")
        for btn in self.chapter_buttons:
            btn.config(state="disabled")
        self.clue_btn.config(state="disabled")
        self._show_welcome()

    def _show_instructions(self):
        text = (
            "1. COMENZAR AVENTURA.\n"
            "2. Lectura de capítulos 1–5.\n"
            "3. Mostrar Pista por capítulo.\n"
            "4. Acusar al final.\n"
            "5. Reiniciar con el botón 'Reiniciar Juego'."
        )
        messagebox.showinfo("Instrucciones", text)

if __name__ == "__main__":
    ClueApp().mainloop()
