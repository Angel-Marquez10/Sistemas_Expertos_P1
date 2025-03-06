class Graph:
    def __init__(self):
        """Inicializa un grafo vacío para la red de calles."""
        self.graph = {}  # Diccionario para almacenar conexiones entre calles y sus distancias.
        self.heuristic = {}  # Diccionario para almacenar valores heurísticos de cada calle.

    def add_street(self, u, v, distance):
        """Agrega una calle entre dos ubicaciones con una distancia determinada."""
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, distance))

    def set_heuristic(self, location, value):
        """Establece la heurística para una ubicación."""
        self.heuristic[location] = value

    def a_star(self, start, goal):
        """Implementación del algoritmo A* para encontrar la ruta óptima."""
        open_list = [(start, 0)]  # Lista de nodos por explorar con sus costos.
        g_cost = {start: 0}  # Costos desde el inicio hasta cada nodo.
        came_from = {start: None}  # Rutas óptimas registradas.

        while open_list:
            # Ordena la lista para seleccionar el nodo con menor costo estimado.
            open_list.sort(key=lambda x: x[1] + self.heuristic.get(x[0], float('inf')))
            current, _ = open_list.pop(0)
            print(f"Visitando: {current}")

            if current == goal:
                path = self._reconstruct_path(came_from, goal)
                print(f"Entrega completada: Ruta óptima -> {path}")
                return path

            for neighbor, distance in self.graph.get(current, []):
                new_cost = g_cost[current] + distance
                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    open_list.append((neighbor, new_cost))
                    came_from[neighbor] = current

        print("No se encontró una ruta hacia el destino.")
        return None

    def _reconstruct_path(self, came_from, current):
        """Reconstruye el camino óptimo hacia el destino."""
        path = []
        while current is not None:
            path.append(current)
            current = came_from[current]
        return path[::-1]

# Ejemplo de uso
if __name__ == "__main__":
    g = Graph()
    
    # Definición de calles y distancias
    g.add_street('Restaurante', 'Calle 1', 3)
    g.add_street('Calle 1', 'Calle 2', 2)
    g.add_street('Calle 2', 'Cliente', 5)
    g.add_street('Restaurante', 'Avenida 1', 4)
    g.add_street('Avenida 1', 'Cliente', 6)
    
    # Definición de heurísticas (distancias aproximadas al destino)
    g.set_heuristic('Restaurante', 7)
    g.set_heuristic('Calle 1', 4)
    g.set_heuristic('Calle 2', 2)
    g.set_heuristic('Avenida 1', 5)
    g.set_heuristic('Cliente', 0)
    
    # Buscar la mejor ruta
    print("Ruta óptima para la entrega:")
    g.a_star('Restaurante', 'Cliente')
