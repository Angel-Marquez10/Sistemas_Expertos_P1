import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

# -----------------------------------
# Definición de preguntas en orden
# -----------------------------------
preguntas = [
    "Inicio",
    "¿Es de la marca Toyota?",
    "¿Funciona con Gasolina?",
    "¿Es un SUV?",
    "¿Tiene 4 puertas?",
    "Fin"
]

# -----------------------------------
# Construcción del grafo dirigido
# -----------------------------------
G = nx.DiGraph()
for nodo in preguntas:
    G.add_node(nodo)

# Conectar cada pregunta con la siguiente: rama Sí y No
conexiones = [
    ("Inicio",                preguntas[1]),
    (preguntas[1],            preguntas[2]),
    (preguntas[2],            preguntas[3]),
    (preguntas[3],            preguntas[4]),
    (preguntas[4],            "Fin")
]
for src, dst in conexiones:
    G.add_edge(src, dst, label="Sí",  color="#2E86C1")
    G.add_edge(src, dst, label="No",  color="#EB984E", style="dashed")

# -----------------------------------
# Dibujar el grafo (top-down)
# -----------------------------------
plt.figure(figsize=(8, 6))
try:
    # Usa Graphviz 'dot' para layout jerárquico
    pos = graphviz_layout(G, prog='dot')
except:
    # Fallback a spring layout si dot no está disponible
    pos = nx.spring_layout(G)

# Dibujar nodos
nx.draw_networkx_nodes(G, pos,
                       node_size=1800,
                       node_color="#AED6F1",
                       edgecolors="#1B4F72",
                       linewidths=1)

# Dibujar etiquetas de nodos
nx.draw_networkx_labels(G, pos,
                        font_size=10,
                        font_weight='bold',
                        font_color="#1B2631")

# Dibujar aristas con estilo
edge_colors  = [G[u][v]['color'] for u,v in G.edges()]
edge_styles  = ['dashed' if G[u][v].get('style')=='dashed' else 'solid' for u,v in G.edges()]
nx.draw_networkx_edges(G, pos,
                       edge_color=edge_colors,
                       style=edge_styles,
                       arrowsize=20,
                       arrowstyle='-|>')

# Dibujar etiquetas de aristas (Sí/No)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos,
                             edge_labels=edge_labels,
                             font_size=9,
                             font_color="#34495E")

plt.title("Árbol de Decisión para 'Adivina el Auto'", fontsize=14, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
