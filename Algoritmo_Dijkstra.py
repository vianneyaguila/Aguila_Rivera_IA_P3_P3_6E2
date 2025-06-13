# Importamos bibliotecas necesarias
import heapq  # Para implementar la cola de prioridad (mínima)
import networkx as nx  # Para trabajar con grafos dirigidos y visualización
import matplotlib.pyplot as plt  # Para mostrar gráficamente el grafo

# Función: Algoritmo de Dijkstra entre nodo origen y destino

def dijkstra_ruta(grafo, inicio, destino):
    """
    Encuentra la ruta más corta entre 'inicio' y 'destino' en un grafo ponderado.
    Retorna la ruta como lista de nodos y la distancia total.
    """

    # Inicializamos las distancias a infinito para todos los nodos
    distancias = {nodo: float('inf') for nodo in grafo}

    # La distancia al nodo de inicio es cero
    distancias[inicio] = 0

    # Diccionario para reconstruir el camino más corto (predecesores)
    predecesores = {nodo: None for nodo in grafo}

    # Conjunto de nodos ya visitados
    visitados = set()

    # Cola de prioridad que guarda (distancia, nodo)
    cola = [(0, inicio)]

    # Bucle principal del algoritmo
    while cola:
        # Sacamos el nodo con la menor distancia conocida
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si ya fue visitado, lo ignoramos
        if nodo_actual in visitados:
            continue

        # Marcamos el nodo como visitado
        visitados.add(nodo_actual)

        # Recorremos todos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            # Calculamos la nueva distancia hasta ese vecino
            nueva_distancia = distancia_actual + peso

            # Si encontramos una mejor ruta, actualizamos
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia       # Actualizamos distancia mínima
                predecesores[vecino] = nodo_actual         # Guardamos el nodo anterior
                heapq.heappush(cola, (nueva_distancia, vecino))  # Agregamos vecino a la cola

  
    # Reconstrucción del camino desde destino al origen

    camino = []  # Lista vacía para guardar el camino más corto
    actual = destino

    # Retrocedemos desde el destino hasta el origen
    while actual is not None:
        camino.insert(0, actual)  # Insertamos al principio para que el orden sea correcto
        actual = predecesores[actual]  # Avanzamos al nodo anterior

    # Si la distancia sigue siendo infinita, no hay camino
    if distancias[destino] == float('inf'):
        print(f"No existe una ruta de {inicio} a {destino}")
        return None, None

    # Mostramos el resultado en consola
    print(f"\n Ruta más corta desde {inicio} a {destino}")
    print(f"Distancia total: {distancias[destino]} km")
    print(f"Ruta: {' → '.join(camino)}")

    return camino, distancias[destino]  # Devolvemos la ruta y su distancia


# Función: Visualización del grafo con ruta resaltada

def graficar_ruta(grafo, ruta_destacada=None):
    """
    Visualiza el grafo y resalta una ruta específica en rojo si se proporciona.
    """

    G = nx.DiGraph()  # Creamos un grafo dirigido

    # Agregamos nodos y aristas con sus pesos al grafo
    for origen in grafo:
        for destino, peso in grafo[origen].items():
            G.add_edge(origen, destino, weight=peso)  # Creamos arista con peso

    # Posiciones de los nodos para una visualización ordenada
    pos = nx.spring_layout(G, seed=42)

    # Obtenemos etiquetas de peso de las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')

    # Colores de las aristas: gris por defecto, rojo si es parte de la ruta más corta
    edge_colors = []
    for u, v in G.edges():
        if ruta_destacada and (u, v) in zip(ruta_destacada, ruta_destacada[1:]):
            edge_colors.append('red')  # Arista pertenece a la ruta más corta
        else:
            edge_colors.append('gray')  # Arista normal

    # Dibujamos el grafo con nodos
    nx.draw(G, pos, with_labels=True,
            node_color='lightblue', node_size=2000,
            font_weight='bold', arrows=True)

    # Dibujamos las etiquetas de los pesos
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Dibujamos las aristas con los colores definidos
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=3)

    # Título del gráfico
    plt.title("Ruta más corta resaltada")
    plt.show()  # Mostramos la visualización

# Definimos el grafo de ejemplo: Rutas logísticas

grafo_montacargas = {
    'BODEGA_CENTRAL': {'CLIENTE_1': 12, 'SUCURSAL_NORTE': 15},
    'CLIENTE_1': {'CLIENTE_2': 8},
    'SUCURSAL_NORTE': {'CLIENTE_3': 7},
    'CLIENTE_2': {'CLIENTE_3': 5},
    'CLIENTE_3': {}  # Nodo final sin salidas
}

# Entrada fija: Puedes cambiar el origen y destino aquí

origen = 'BODEGA_CENTRAL'  # Nodo de inicio
destino = 'CLIENTE_3'      # Nodo de destino

# Ejecutamos Dijkstra para encontrar la ruta más corta
camino, distancia_total = dijkstra_ruta(grafo_montacargas, origen, destino)

# Si se encontró camino, lo graficamos
if camino:
    graficar_ruta(grafo_montacargas, camino)
