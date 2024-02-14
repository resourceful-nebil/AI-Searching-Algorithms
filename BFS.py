from collections import deque


def bfs(graph, start_node):
    visited = []  
    queue = deque([start_node])  

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            print("Visited node:", node)

            neighbors = graph[node]
            num_neighbors = len(neighbors)
            print("Number of neighbors for node", node, ":", num_neighbors)

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


graph = {}
num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    node = input("Enter node: ")
    num_neighbors = int(input("Enter the number of neighbors for node " + node + ": "))
    neighbors = []
    for j in range(num_neighbors):
        neighbor = input("Enter neighbor " + str(j+1) + " for node " + node + ": ")
        neighbors.append(neighbor)
    graph[node] = neighbors
    print(graph)
start_node = input("Enter the starting node: ")


print("\nBreadth-First Search:")
path = bfs(graph, start_node)
print("Path of nodes:", path)

