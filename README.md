# Algoritmo de Dijkstra

## ¿Qué es?

Es una técnica de búsqueda que encuentra la ruta más corta desde un nodo de origen a todos los demás nodos en un gráfico con pesos no negativos.

## Propósito y Usos

- Permite encontrar la ruta más corta entre los nodos de un grafo.
- Específicamente, se puede hallar el camino más corto desde un nodo llamado "nodo de origen" a todos los demás nodos.
- Este algoritmo es usado por dispositivos GPS para determinar la ruta óptima entre la ubicación actual y un destino.
- Optimiza el tráfico de red.
- Calcula costos mínimos en proyectos.
- Determina rutas óptimas en videojuegos y simuladores.

## Aspectos básicos del algoritmo de Dijkstra

- Inicia en el nodo que elijas y analiza el grafo para encontrar el camino más corto.
- Mantiene un registro de la distancia conocida más corta desde el nodo de origen hasta cada nodo.
- Una vez que el algoritmo ha encontrado el camino más corto hacia un nodo, este se marca como "visitado".
- El proceso continúa hasta que todos los nodos del grafo han sido añadidos al camino más corto.

## Requisitos

- Solo puede aplicarse a grafos con aristas (conexiones) cuyos pesos sean positivos.
- Es necesario que el grafo tenga todos sus valores en las aristas sin pesos negativos.
- Se requiere un nodo de origen.
- Se necesita información sobre las aristas y sus respectivos pesos (o distancias).
