# Implementaciones de búsqueda en grafos para encontrar la ruta más corta
# Algoritmos: Búsqueda de Costo Uniforme (UCS), A* Tree Search, A* Graph Search y Greedy Best-First Search

import heapq

def uniform_cost_search(graph, start, goal):
    """
    Búsqueda de costo uniforme (UCS) para encontrar la ruta más corta.
    """
    priority_queue = [(0, start)]  # (costo, nodo)
    visited = set()
    
    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return cost
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))
    
    return float("inf")  # No se encontró camino


def a_star_tree_search(graph, start, goal, heuristic):
    """
    A* Tree Search para encontrar la ruta más corta.
    """
    priority_queue = [(heuristic[start], 0, start)]  # (f(n), g(n), nodo)
    
    while priority_queue:
        _, cost, node = heapq.heappop(priority_queue)
        
        if node == goal:
            return cost
        
        for neighbor, weight in graph.get(node, []):
            heapq.heappush(priority_queue, (cost + weight + heuristic[neighbor], cost + weight, neighbor))
    
    return float("inf")  # No se encontró camino


def a_star_graph_search(graph, start, goal, heuristic):
    """
    A* Graph Search con memoria de nodos visitados.
    """
    priority_queue = [(heuristic[start], 0, start)]  # (f(n), g(n), nodo)
    visited = {}
    
    while priority_queue:
        _, cost, node = heapq.heappop(priority_queue)
        
        if node == goal:
            return cost
        
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        
        for neighbor, weight in graph.get(node, []):
            heapq.heappush(priority_queue, (cost + weight + heuristic[neighbor], cost + weight, neighbor))
    
    return float("inf")  # No se encontró camino


def greedy_best_first_search(graph, start, goal, heuristic):
    """
    Búsqueda Greedy Best-First basada solo en la heurística.
    """
    priority_queue = [(heuristic[start], start)]  # (h(n), nodo)
    visited = set()
    
    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        
        if node == goal:
            return True  # Encontró el objetivo
        
        if node in visited:
            continue
        visited.add(node)
        
        for neighbor, _ in graph.get(node, []):
            heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
    
    return False  # No se encontró camino

# Ejemplo de uso
graph_example = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3), ('G', 4)],
    'D': [('H', 3)],
    'E': [('H', 6)],
    'F': [('I', 4)],
    'G': [('J', 2)],
    'H': [('I', 1)],
    'I': [('J', 1)],
    'J': []
}

heuristic_example = {
    'A': 7, 'B': 6, 'C': 3, 'D': 5, 'E': 4, 'F': 2, 'G': 1, 'H': 3, 'I': 1, 'J': 0
}

start_node = 'A'
goal_node = 'J'

print("Costo UCS:", uniform_cost_search(graph_example, start_node, goal_node))
print("Costo A* Tree:", a_star_tree_search(graph_example, start_node, goal_node, heuristic_example))
print("Costo A* Graph:", a_star_graph_search(graph_example, start_node, goal_node, heuristic_example))
print("Encontró camino Greedy:", greedy_best_first_search(graph_example, start_node, goal_node, heuristic_example))

