
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'D': 4, 'E': 2},
    'C': {'F': 3},
    'D': {'G': 6},
    'E': {'H': 5},
    'F': {'I': 8},
    'G': {},
    'H': {},
    'I': {}
}

heuristics = {
    'A': 10,
    'B': 7,
    'C': 5,
    'D': 3,
    'E': 5,
    'F': 4,
    'G': 2,
    'H': 2,
    'I': 0
}

# Implement Best-First (Greedy) Search algorithm
def best_first_search(start, goal):
    # Create an empty priority queue to store the nodes to be explored
    priority_queue = []
    visited = set()

    # Add the start node to the priority queue with its heuristic value as priority
    priority_queue.append((start, 0))
    visited.add(start)

    while priority_queue:
        # Get the node with the highest priority from the priority queue
        current_node, current_cost = priority_queue.pop(0)

        # Check if the current node is the goal node
        if current_node == goal:
            return current_cost

        # Explore the neighbors of the current node
        for neighbor, cost in graph[current_node].items():
            # Calculate the priority of the neighbor based on its heuristic value
            priority = heuristics[neighbor]
            # Add the neighbor to the priority queue if it has not been visited
            if neighbor not in visited:
                priority_queue.append((neighbor, current_cost + cost))
                visited.add(neighbor)

        # Sort the priority queue based on priority (heuristic value)
        priority_queue.sort(key=lambda x: x[1])

    return float('inf')

# Test the best_first_search function
start_node = 'A'
goal_node = 'I'
optimal_cost = best_first_search(start_node, goal_node)
print("Optimal path cost:", optimal_cost)