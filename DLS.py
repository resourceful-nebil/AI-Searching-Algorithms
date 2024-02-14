# Enter the number of nodes: 5
# Enter a node: A
# Enter the number of neighbors: 2
# Enter a neighbor: S
# Enter a neighbor: B
# Enter a node: S
# Enter the number of neighbors: 1
# Enter a neighbor: C
# Enter a node: B
# Enter the number of neighbors: 1
# Enter a neighbor: C
# Enter a node: C
# Enter the number of neighbors: 0
# Enter a node: D
# Enter the number of neighbors: 0
# Enter the start node: A
# Enter the goal node: C
# Enter the depth limit: 2
# Goal node found within the depth limit.
def depth_limited_search(graph, start, goal, depth_limit):
    visited = set()
    result = dls(graph, start, goal, visited, depth_limit)
    return result

def dls(graph, current, goal, visited, depth_limit):
    if current == goal:
        return True

    if depth_limit <= 0:
        return False

    visited.add(current)

    if current not in graph:
        return False

    for neighbor in graph[current]:
        if neighbor not in visited:
            result = dls(graph, neighbor, goal, visited, depth_limit - 1)
            if result:
                return True

    return False

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
depth_limit = int(input("Enter the depth limit: "))

# Perform the depth-limited search
result = depth_limited_search(graph, start_node, goal_node, depth_limit)

# Print the result
if result:
    print("Goal node found within the depth limit.")
else:
    print("Goal node was not found within the depth limit.")



# In this code, the user is asked to input the number of nodes, their connections, the start node, the goal node, and the depth limit. The Depth-Limited Search algorithm is implemented using a recursive function `dls()` that performs depth-limited search from the start node to the goal node. The code is structured to be easily understood and prints the appropriate message indicating whether the goal node was found within the depth limit or not.

