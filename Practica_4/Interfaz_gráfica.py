# src/ui.py
import tkinter as tk
from tkinter import messagebox
from Logica_del_juego import Game
from Historias import CHARACTERS, LOCATIONS, WEAPONS

class ClueApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Simulador CLUE')
        self.geometry('600x400')
        self.game = Game()
        self._build_intro()

    def _build_intro(self):
        # Texto introductorio y botón de empezar
        self.clear()
        label = tk.Label(self, text=self.game.get_intro(), wraplength=500)
        label.pack(pady=20)
        start_btn = tk.Button(self, text='Empezar Partida', command=self._build_menu)
        start_btn.pack()

    def _build_menu(self):
        # Menú principal con opciones
        self.clear()
        tk.Button(self, text='Hacer sugerencia', command=self._build_suggest).pack(pady=10)
        tk.Button(self, text='Ver pista', command=self._show_last_hint).pack(pady=10)
        tk.Button(self, text='Acusar', command=self._build_accuse).pack(pady=10)

    def _build_suggest(self):
        self.clear()
        tk.Label(self, text='Selecciona personaje, arma y locación:').pack()
        # Dropdowns
        self.char_var = tk.StringVar(value=list(CHARACTERS.keys())[0])
        tk.OptionMenu(self, self.char_var, *CHARACTERS.keys()).pack()
        self.weap_var = tk.StringVar(value=list(WEAPONS.keys())[0])
        tk.OptionMenu(self, self.weap_var, *WEAPONS.keys()).pack()
        self.loc_var = tk.StringVar(value=list(LOCATIONS.keys())[0])
        tk.OptionMenu(self, self.loc_var, *LOCATIONS.keys()).pack()
        tk.Button(self, text='Enviar sugerencia', command=self._do_suggest).pack(pady=10)
        tk.Button(self, text='Volver', command=self._build_menu).pack()

    def _do_suggest(self):
        hint = self.game.suggest(self.char_var.get(), self.weap_var.get(), self.loc_var.get())
        tips = [f"Personaje: {'✔️' if hint['character'] else '❌'}",
                f"Arma: {'✔️' if hint['weapon'] else '❌'}",
                f"Locación: {'✔️' if hint['location'] else '❌'}"]
        messagebox.showinfo('Pistas', '\n'.join(tips))
        self._build_menu()

    def _show_last_hint(self):
        if not self.game.guesses:
            messagebox.showwarning('Sin sugerencias', 'Primero haz una sugerencia.')
        else:
            self._do_suggest()  # muestra la última pista de nuevo

    def _build_accuse(self):
        self.clear()
        tk.Label(self, text='¡Haz tu acusación final!').pack()
        self.ac_char = tk.StringVar(value=list(CHARACTERS.keys())[0])
        tk.OptionMenu(self, self.ac_char, *CHARACTERS.keys()).pack()
        self.ac_weap = tk.StringVar(value=list(WEAPONS.keys())[0])
        tk.OptionMenu(self, self.ac_weap, *WEAPONS.keys()).pack()
        self.ac_loc = tk.StringVar(value=list(LOCATIONS.keys())[0])
        tk.OptionMenu(self, self.ac_loc, *LOCATIONS.keys()).pack()
        tk.Button(self, text='Acusar', command=self._do_accuse).pack(pady=10)
        tk.Button(self, text='Volver', command=self._build_menu).pack()

    def _do_accuse(self):
        correct = self.game.accuse(self.ac_char.get(), self.ac_weap.get(), self.ac_loc.get())
        if correct:
            messagebox.showinfo('¡Correcto!', self.game.get_final_story())
        else:
            messagebox.showerror('Fallido', 'Acusación incorrecta. Fin de la partida.')
        self.destroy()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    ClueApp().mainloop()