# Enter the number of nodes: 7
# Enter a node: A
# Enter the number of neighbors: 2
# Enter a neighbor: C
# Enter a neighbor: I 
# Enter a node: C
# Enter the number of neighbors: 2
# Enter a neighbor: B
# Enter a neighbor: E
# Enter a node: I
# Enter the number of neighbors: 2
# Enter a neighbor: H
# Enter a neighbor: J
# Enter a node: B
# Enter the number of neighbors: 0
# Enter a node: E
# Enter the number of neighbors: 0
# Enter a node: H
# Enter the number of neighbors: 0
# Enter a node: J
# Enter the number of neighbors: 0
# Enter the start node: A
# Enter the goal node: J
# Path found: ['A', 'I', 'J']


def dfs(graph, start, goal):
    stack = [(start, [start])]  # Initialize stack with start node and path

    while stack:
        current, path = stack.pop()  # Retrieve the current node and its path

        if current == goal:
            return path  # Return the path if goal node is found

        if current not in graph:
            continue  # Skip if current node has no neighbors

        for neighbor in graph[current]:
            if neighbor not in path:  # Avoid revisiting nodes in the current path
                stack.append((neighbor, path + [neighbor]))  # Add neighbor to the stack with updated path

    return []  # Return an empty list if no path is found


# Prompt the user to input the nodes and their connections
graph = {}

num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter a node: ")
    num_neighbors = int(input("Enter the number of neighbors: "))

    neighbors = []
    for _ in range(num_neighbors):
        neighbor = input("Enter a neighbor: ")
        neighbors.append(neighbor)

    graph[node] = neighbors

# Prompt the user to input the start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Perform the depth-first search
result = dfs(graph, start_node, goal_node)

# Print the result
if result:
    print("Path found:", result)
else:
    print("No path found.")


# In this code, the user is asked to input the number of nodes, their connections, 
# the start node, and the goal node. The DFS algorithm is implemented using a stack to
#  keep track of nodes to visit. The code retrieves the current node and its path from
#  the stack, checks if it is the goal node, and explores its neighbors.
#  The algorithm continues until it finds the goal node or exhausts all possible paths. 
# Finally, the code prints the path if it is found, or a message indicating that no path is found.
