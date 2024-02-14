import heapq

def heuristic(node, goal_node):
    # Placeholder heuristic function; replace with an appropriate one for your problem
    return 0

def ao_star(graph, start_node, goal_node):
    if start_node not in graph or goal_node not in graph:
        print("Invalid start or goal node.")
        return []

    visited = set()
    priority_queue = [(0, start_node, [start_node])]  # Priority queue format: (f(n), node, path)

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)

        if node not in visited:
            visited.add(node)
            print("Visited node:", node)

            if node == goal_node:
                print("Goal node reached!")
                break

            for neighbor, cost in graph[node].items():
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    g = cost + heuristic(neighbor, goal_node)
                    f = g + heuristic(goal_node, goal_node)  # Use heuristic(goal_node, goal_node) only once
                    heapq.heappush(priority_queue, (f, neighbor, new_path))

    return path

# neghbour and cost to reach them
graph = {
    'S': {'A': 2, 'B': 4}, 
    'A': {'C': 7},
    'B': {'C': 1, 'D': 5},
    'C': {'D': 2},
    'D': {'G': 3},
    'G': {},
}

start_node = 'S'
goal_node = 'G'

print("AO* Search:")
path = ao_star(graph, start_node, goal_node)
print("Path of nodes:", path)
