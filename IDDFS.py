# In this code, start_node represents the starting node of the graph, goal_node is
#  the node we want to reach, and max_depth represents the maximum depth to search. 
# The IDDFS function iterates from depth 0 to max_depth, calling the DLS function for each
# depth level.

# The DLS function performs a depth-limited search starting from the current_node until it 
# reaches the goal_node or the depth limit is reached. It keeps track of visited nodes in 
# the visited set and adds the nodes encountered to the path list.

# If the goal node is found, the function appends it to the path and returns True.
#  Otherwise, it continues to explore the neighbors of the current node until all possibilities 
# are exhausted.

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.neighbors = []

# # Perform Iterative Deepening Depth-First Search
# def IDDFS(start_node, goal_node, max_depth):
#     for depth in range(max_depth + 1):
#         visited = set()
#         path = []
#         if DLS(start_node, goal_node, depth, visited, path):
#             return path
#     return None

# # Recursive Depth-Limited Search
# def DLS(current_node, goal_node, depth, visited, path):
#     if current_node == goal_node:
#         path.append(current_node)
#         return True
#     if depth <= 0:
#         return False
#     visited.add(current_node)
#     for neighbor in current_node.neighbors:
#         if neighbor not in visited:
#             path.append(current_node)
#             if DLS(neighbor, goal_node, depth - 1, visited, path):
#                 return True
#             path.pop()
#     return False

# # Create a sample graph for testing
# def create_sample_graph():
#     node_A = Node("A")
#     node_B = Node("B")
#     node_C = Node("C")
#     node_D = Node("D")
#     node_E = Node("E")

#     node_A.neighbors = [node_B, node_C]
#     node_B.neighbors = [node_D, node_E]
#     node_C.neighbors = [node_D]
#     node_D.neighbors = []
#     node_E.neighbors = [node_D]

#     return node_A

# # Example usage
# graph = create_sample_graph()
# start_node = graph
# goal_node = graph.neighbors[1].neighbors[0]  # Goal node is "D"
# max_depth = 3

# path = IDDFS(start_node, goal_node, max_depth)
# if path:
#     path = [node.value for node in path[::-1]]  # Reverse the path
#     print("Path found:", "->".join(path))
# else:
#     print("Path not found.")


# In this expanded version, I've added a `Node` class to represent the nodes in the graph.
#  Each node has a `value` and a list of `neighbors` representing the adjacent nodes.

# The `create_sample_graph` function creates a sample graph with nodes A, B, C, D, and E, and 
# establishes the connections among them.

# In the example usage section, we create the sample graph, set the `start_node

# Enter the number of nodes: 7
# Enter a node: A
# Enter the number of neighbors: 2
# Enter a neighbor: B
# Enter a neighbor: C
# Enter a node: B
# Enter the number of neighbors: 2
# Enter a neighbor: D
# Enter a neighbor: E
# Enter a node: C
# Enter the number of neighbors: 2
# Enter a neighbor: F
# Enter a neighbor: G
# Enter a node: D
# Enter the number of neighbors: 0
# Enter a node: E
# Enter the number of neighbors: 0
# Enter a node: F
# Enter the number of neighbors: 0
# Enter a node: G
# Enter the number of neighbors: 0
# Enter the start node: A
# Enter the goal node: E
# Enter the depth limit: 2
# Goal node found within the depth limit!

# --------------------------------------------------------

# Enter the number of nodes: 3
# Enter a node: A
# Enter the number of neighbors: 2
# Enter a neighbor: B
# Enter a neighbor: C
# Enter a node: B
# Enter the number of neighbors: 0
# Enter a node: C
# Enter the number of neighbors: 0
# Enter the start node: A
# Enter the goal node: C
# Enter the depth limit: 0
# Goal node not found within the depth limit!
graph = {}

def depth_limited_dfs(node, goal, depth_limit):
    if node == goal:
        return True

    if depth_limit <= 0:
        return False

    if node not in graph:
        return False

    for neighbor in graph[node]:
        if depth_limited_dfs(neighbor, goal, depth_limit - 1):
            return True

    return False

def iterative_deepening_dfs(start, goal, limit):
    for depth_limit in range(limit + 1):
        if depth_limited_dfs(start, goal, depth_limit):
            return True

    return False

# Prompt the user to input the nodes and their connections
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter a node: ")
    num_neighbors = int(input("Enter the number of neighbors: "))

    neighbors = []
    for _ in range(num_neighbors):
        neighbor = input("Enter a neighbor: ")
        neighbors.append(neighbor)
    
    graph[node] = neighbors

# Prompt the user to input the start and goal nodes, as well as the depth limit
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
depth_limit = int(input("Enter the depth limit: "))

# Perform the IDDFS
result = iterative_deepening_dfs(start_node, goal_node, depth_limit)

# Print the result
if result:
    print("Goal node found within the depth limit!")
else:
    print("Goal node not found within the depth limit!")

# In this code, the user is asked to input the number of nodes, their connections, the start and goal nodes, and the depth limit. The IDDFS algorithm is implemented using a depth-limited search approach. The code is structured to be easily understood and prints the appropriate message based on whether the goal node is found within the specified depth limit or not.

