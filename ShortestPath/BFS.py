# Implementación de BFS para encontrar el camino más corto en una matriz
# Utilizando búsqueda en anchura (BFS)

from collections import deque

def bfs_shortest_path(grid, start, treasure):
    """
    Encuentra el camino más corto desde la posición inicial hasta el tesoro
    utilizando búsqueda en anchura (BFS).
    
    Parámetros:
    grid: Lista de listas representando la matriz de la isla.
    start: Tupla (x, y) con la posición inicial.
    treasure: Tupla (x, y) con la posición del tesoro.
    
    Retorna:
    Número mínimo de pasos para alcanzar el tesoro o -1 si no hay camino.
    """
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
    queue = deque([(start[0], start[1], 0)])  # (x, y, pasos)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, steps = queue.popleft()
        
        if (x, y) == treasure:
            return steps
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, steps + 1))
                visited.add((new_x, new_y))
    
    return -1  # No se encontró camino

# Ejemplo de uso:
isla_1 = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

isla_2 = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

pos_inicio_1 = (0, 0)
pos_tesoro_1 = (3, 3)
pos_inicio_2 = (2, 0)
pos_tesoro_2 = (4, 4)

pasos_1 = bfs_shortest_path(isla_1, pos_inicio_1, pos_tesoro_1)
pasos_2 = bfs_shortest_path(isla_2, pos_inicio_2, pos_tesoro_2)

print("Pasos mínimos en el primer ejemplo:", pasos_1)
print("Pasos mínimos en el segundo ejemplo:", pasos_2)
