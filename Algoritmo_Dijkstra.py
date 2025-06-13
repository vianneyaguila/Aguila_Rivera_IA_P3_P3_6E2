import heapq #Permite usar una cola de prioridad
import networkx as nx #networkx trabaja con gráficos
import matplotlib.pyplot as plt # Para mostrar el gráfico

# ------------------------
# Dijkstra paso a paso
# ------------------------

def dijkstra(grafo, inicio): #grafo: Diccionario que representa las conexiones (rutas) entre nosdos 
    #inicio: el nodo desde donde empieza el cálculo (BODEGA CENTRAL)
    """
    Algoritmo de Dijkstra con salida paso a paso en consola.
    grafo: diccionario de adyacencia con pesos.
    inicio: nodo de inicio.
    """
    distancias = {nodo: float('inf') for nodo in grafo} #crea un diccionario distancias, con cada nodo infinito, que después se irá actulizando
    distancias[inicio] = 0 # Ka distancia del nodo de inicio a sí mismo se establece en 0
    visitados = set() # para llevar el control de los nodos que ya se procesaron
    cola = [(0, inicio)] #Una cola de prioridad donde se guardan nodos con su distancia real mínima.

    print(f"\n🟢 Inicio desde: {inicio}")
    print("-" * 50)

    while cola: #Mientras haya nudos en la cola, saca el nudo con la menor distancia conocida
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados: # Si ya se ha visitado ese nudo, se salta. 
            continue

        print(f"Visitando: {nodo_actual}") #Muestra en consola que nodo se esta evaluando y su distancia real mínima. Se marca como visitado para no repetirlo.
        print(f"Distancia actual mínima: {distancia_actual}")
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items(): #Se itera sobre los vecinos directores del nodo actual, pero es la distancia entre el nodo actual y su vecino.
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]: #Si se encuntra una mejor ruta, se actualiza la distancia.
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
                print(f"  ↳ Actualizando distancia de {vecino} a {nueva_distancia}")

    print("\n✅ Resultado Final:") #Se imprimen las distancias más cortas desde el nodo de inicio a todos los demás. 
    for nodo, distancia in distancias.items():
        print(f"Distancia mínima a {nodo}: {distancia} km")

    return distancias

# ------------------------
# Visualización gráfica
# ------------------------

def graficar_rutas(grafo): #Representa las rutas.
    """
    Muestra un grafo visual con pesos.
    """
    G = nx.DiGraph()

    # Agrega los nodos y aristas con pesos
    for origen in grafo: #rrecorre el diccionario del grafo y añade cada ruta como arista con su peso.
        for destino, peso in grafo[origen].items():
            G.add_edge(origen, destino, weight=peso)

    pos = nx.spring_layout(G, seed=42) #posiciona los nodos automaticamente de forma visualmente clara. Dibuja el grafo con etiquetas y flechas, mostrando los pesos de las rutas.
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_weight='bold', arrows=True)
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    plt.title("Rutas logísticas de montacargas") #Muestra la gráfica con un titulo
    plt.show()

# ------------------------
# Ejemplo adaptado: Empresa de montacargas
# ------------------------

grafo_montacargas = {
    'BODEGA_CENTRAL': {'CLIENTE_1': 12, 'SUCURSAL_NORTE': 15},
    'CLIENTE_1': {'CLIENTE_2': 8},
    'SUCURSAL_NORTE': {'CLIENTE_3': 7},
    'CLIENTE_2': {'CLIENTE_3': 5},
    'CLIENTE_3': {}
} #Este representa los puntos geográficos #Los valores son distancias(pueden ser Km, timepo o incluso costos.)

# Ejecutar algoritmo
resultado = dijkstra(grafo_montacargas, 'BODEGA_CENTRAL')
#Se llama la algoritmo desde BODEGA_CENTRAL y muestra la gráfica
# Mostrar grafo visual
graficar_rutas(grafo_montacargas)
