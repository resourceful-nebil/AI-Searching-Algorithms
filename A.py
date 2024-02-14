
heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 2,
    'G': 6,
    'H': 4,
    'I': 0
}
# Define the graph dictionary
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 6, 'G': 8},
    'D': {'H': 7},
    'E': {},
    'F': {'I': 3},
    'G': {},
    'H': {'I': 2},
    'I': {}
}

# Rest of the code goes here...

# Testing the A* search algorithm

def astar_search(start, goal):
    # Create an empty priority queue to store the nodes to be explored
    priority_queue = []
    visited = set()
    path_cost = {start: 0}
    path = {start: [start]}  # Store the path to each node

    # Add the start node to the priority queue with its total cost as priority
    priority_queue.append((start, 0 + heuristics[start]))
    visited.add(start)

    while priority_queue:
        # Get the node with the highest priority from the priority queue
        current_node, current_cost = priority_queue.pop(0)

        # Check if the current node is the goal node
        if current_node == goal:
            optimal_path = path[current_node]
            print("Optimal path nodes:", optimal_path)
            return current_cost

        # Explore the neighbors of the current node
        for neighbor, cost in graph[current_node].items():
            # Calculate the total cost to reach the neighbor
            total_cost = path_cost[current_node] + cost

            # Check if the neighbor has not been visited or a better path is found
            if neighbor not in visited or total_cost < path_cost[neighbor]:
                path_cost[neighbor] = total_cost
                # Calculate the priority of the neighbor as the sum of path cost and heuristic value
                priority = total_cost + heuristics[neighbor]
                # Add the neighbor to the priority queue
                priority_queue.append((neighbor, priority))
                visited.add(neighbor)
                # Update the path to the neighbor
                path[neighbor] = path[current_node] + [neighbor]
                print("Optimal path nodes:", path[neighbor])

        # Sort the priority queue
        priority_queue.sort(key=lambda x: x[1])

start_node = 'A'
goal_node = 'I'
optimal_cost = astar_search(start_node, goal_node)
print("Optimal cost:", optimal_cost)
