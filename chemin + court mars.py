from __future__ import annotations
import math
from itertools import permutations
import random

class Node:
    def __init__(self, value: str, coordinates: tuple[int, int]) -> None:
        self.value = value
        self.coordinates = coordinates
        self.children = []
    
    def add_child(self, child: Node) -> None:
        self.children.append(child)
    
    def __str__(self) -> str:
        return self.value

    def find_shortest_path(self) -> list[Node]:
        shortest_path = None
        
        # Generate all permutations of points 1, 2, and 3
        permutations_123 = permutations(['1', '2', '3'])
        
        for perm in permutations_123:
            current_path = [self] + [Node(value, coordinates[value]) for value in perm]
            
            # Check if the current path is shorter than the shortest path found so far
            if shortest_path is None or self.path_length(current_path) < self.path_length(shortest_path):
                shortest_path = current_path
        
        return shortest_path
    
    def path_length(self, path: list[Node]) -> float:
        length = 0.0
        
        for i in range(len(path) - 1):
            length += distance(path[i].coordinates, path[i+1].coordinates)
        
        return length

# Coordonnées aléatoires pour les points 1, 2 et 3
coordinates = {
    '0': (0, 0),  # Coordonnées du point 0 (Origine)
    '1': (random.randint(1, 10), random.randint(1, 10)),  # Coordonnées aléatoires pour le point 1
    '2': (random.randint(1, 10), random.randint(1, 10)),  # Coordonnées aléatoires pour le point 2
    '3': (random.randint(1, 10), random.randint(1, 10))   # Coordonnées aléatoires pour le point 3
}

# Fonction pour calculer la distance entre deux points
def distance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Création des nœuds de l'arbre
node0 = Node('0', coordinates['0'])
node1 = Node('1', coordinates['1'])
node2 = Node('2', coordinates['2'])
node3 = Node('3', coordinates['3'])

# Construction de l'arbre
node0.add_child(node1)
node1.add_child(node2)
node2.add_child(node3)

# Recherche du chemin le plus rapide en 4 étapes
shortest_path = node0.find_shortest_path()

# Affichage du chemin le plus court
if shortest_path is None:
    print("Aucun chemin trouvé en 4 étapes.")
else:
    print("Chemin le plus rapide en parcours en profondeur (4 étapes) :")
    for node in shortest_path:
        print(node)
