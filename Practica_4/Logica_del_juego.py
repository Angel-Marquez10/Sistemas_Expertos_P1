# src/game.py
import random
from Historias import CHARACTERS, LOCATIONS, WEAPONS, STORIES

class Game:
    def __init__(self):
        # Convertimos claves a listas
        self.char_keys = list(CHARACTERS.keys())
        self.loc_keys = list(LOCATIONS.keys())
        self.weap_keys = list(WEAPONS.keys())

        # Solución aleatoria combinada:
        self.solution = self._random_solution()
        self.guesses = []  # Historial de sugerencias

    def _random_solution(self):
        return (
            random.choice(self.char_keys),
            random.choice(self.weap_keys),
            random.choice(self.loc_keys)
        )

    def suggest(self, char_key, weap_key, loc_key):
        """Registrar sugerencia y devolver pista booleana si coincide alguna parte."""
        self.guesses.append((char_key, weap_key, loc_key))
        # Devolver pistas: True si alguno coincide con la solución
        return {
            'character': char_key == self.solution[0],
            'weapon': weap_key == self.solution[1],
            'location': loc_key == self.solution[2]
        }

    def accuse(self, char_key, weap_key, loc_key):
        """Verifica acusación definitiva; devuelve True/False"""
        return (char_key, weap_key, loc_key) == self.solution

    def get_intro(self):
        return "Bienvenido a la Mansión Clue. ¡Descubre al culpable, el arma y la locación!"

    def get_final_story(self):
        key = self.solution
        title, text = STORIES[key]
        return f"\n---\n{title}\n{text}\n---"