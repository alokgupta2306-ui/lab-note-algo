import numpy as np
import random

# Nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Distance matrix
distance = np.array([
    [0, 2, 4, 0, 0, 0],  # A
    [2, 0, 1, 3, 0, 0],  # B
    [4, 1, 0, 0, 2, 0],  # C
    [0, 3, 0, 0, 1, 5],  # D
    [0, 0, 2, 1, 0, 2],  # E
    [0, 0, 0, 5, 2, 0]   # F
])

# Parameters
num_ants = 20
iterations = 50
alpha = 1
beta = 2
evaporation = 0.5

# Initial pheromone
pheromone = np.ones((6, 6))

# Source and destination
source = 0       # A
destination = 5  # F

def find_path():
    current = source
    path = [current]

    while current != destination:

        # Find connected nodes
        neighbors = [
            i for i in range(6)
            if distance[current][i] > 0 and i not in path
        ]

        if not neighbors:
            return None

        # Calculate probability
        probabilities = []
        for next_node in neighbors:
            tau = pheromone[current][next_node]
            eta = 1 / distance[current][next_node]
            probability = (tau ** alpha) * (eta ** beta)
            probabilities.append(probability)

        # Normalize probabilities
        probabilities = np.array(probabilities)
        probabilities = probabilities / probabilities.sum()

        # Select next node
        next_node = random.choices(
            neighbors,
            weights=probabilities,
            k=1
        )[0]

        path.append(next_node)
        current = next_node

    return path

best_path = None
best_length = float('inf')

# ACO iterations
for iteration in range(iterations):
    paths = []

    # Generate paths
    for ant in range(num_ants):
        path = find_path()

        if path is not None:
            length = 0
            for i in range(len(path) - 1):
                length += distance[path[i]][path[i + 1]]
            paths.append((path, length))

            # Store best path
            if length < best_length:
                best_length = length
                best_path = path

    # Evaporation
    pheromone *= (1 - evaporation)

    # Deposit pheromone
    for path, length in paths:
        deposit = 1 / length
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

# Display result
print("Ant Colony Optimization")
print("-----------------------")
print("Source :", nodes[source])
print("Destination :", nodes[destination])
print("Best Path :", end=" ")
for node in best_path:
    print(nodes[node], end=" ")
print()
print("Path Length :", best_length)
