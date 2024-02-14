# Enter the number of nodes: 7
# Enter a node: D 
# Enter the number of neighbors: 1
# Enter a neighbor: B
# Enter a node: B
# Enter the number of neighbors: 3
# Enter a neighbor: D
# Enter a neighbor: E
# Enter a neighbor: A
# Enter a node: E
# Enter the number of neighbors: 1
# Enter a neighbor: B
# Enter a node: A
# Enter the number of neighbors: 3
# Enter a neighbor: B
# Enter a neighbor: C
# Enter a neighbor: E
# Enter a node: C
# Enter the number of neighbors: 3
# Enter a neighbor: A
# Enter a neighbor: F
# Enter a neighbor: G
# Enter a node: F
# Enter the number of neighbors: 1
# Enter a neighbor: C
# Enter a node: G
# Enter the number of neighbors: 1
# Enter a neighbor: C
# Enter the start node: D
# Enter the goal node: G 
# Front search and backward search meet at node: A


def bidirectional_search(graph, start, goal):
    # Initialize the forward and backward queues
    forward_queue = [start]
    forward_visited = set([start])

    backward_queue = [goal]
    backward_visited = set([goal])

    while forward_queue and backward_queue:
        # Perform forward search
        current_forward = forward_queue.pop(0)

        if current_forward in backward_visited:
            return current_forward

        if current_forward not in graph:
            continue

        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited.add(neighbor)

        # Perform backward search
        current_backward = backward_queue.pop(0)

        if current_backward in forward_visited:
            return current_backward

        if current_backward not in graph:
            continue

        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)
                backward_visited.add(neighbor)

    return None

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

# Perform the bidirectional search
result = bidirectional_search(graph, start_node, goal_node)

# Print the result
if result:
    print("Front search and backward search meet at node:", result)
else:
    print("Front search and backward search do not meet.")


# n this code, the user is asked to input the number of nodes, their connections, 
# the start node, and the goal node. The Bidirectional Search algorithm is implemented
#  using two queues: one for the forward search from the start node and another for the 
# backward search from the goal node. The code is structured to be easily understood and 
# prints the appropriate message indicating whether
#  the front search and backward search meet at a node or not.

