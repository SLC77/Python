from __future__ import annotations
import math
import random

class Node:
    def __init__(self, value: str, coordinates: tuple[int, int]) -> None:
        self.value = value
        self.coordinates = coordinates
        self.child = None
    
    def add_child(self, child: Node) -> None:
        self.child = child
    
    def __str__(self) -> str:
        return self.value

    def path_length(self, path: list[Node]) -> float:
        length = 0.0
        
        for i in range(len(path) - 1):
            length += self.distance(path[i].coordinates, path[i+1].coordinates)
        
        return length

    def distance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
# Coordonnées aléatoires pour les points 1, 2 et 3
coordinates = {
    '0': (0, 0),  # Coordonnées du point 0 (Origine)
     '1': (49, 3),  # Coordonnées aléatoires pour le point 1
    '2': (6, 15),  # Coordonnées aléatoires pour le point 2
    '3': (49, 25)   # Coordonnées aléatoires pour le point 3
}

# Création des nœuds de l'arbre
node0 = Node('0', coordinates['0'])
node1 = Node('1', coordinates['1'])
node2 = Node('2', coordinates['2'])
node3 = Node('3', coordinates['3'])

# Construction de l'arbre
node0.add_child(node1)
node1.add_child(node2)
node2.add_child(node3)

# Permutation aléatoire des nœuds
nodes = [node0, node1, node2, node3]
random.shuffle(nodes)

# Recherche du chemin le plus rapide en 4 étapes
shortest_path = nodes[:4]

# Affichage du chemin le plus court
if shortest_path:
    print("Chemin le plus rapide (4 étapes) :")
    for node in shortest_path:
        print(node)
else:
    print("Aucun chemin trouvé en 4 étapes.")
