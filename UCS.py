# Enter the number of nodes: 5
# Enter the node: S
# Enter the number of neighbors for node S: 2
# Enter the neighbor and its cost (separated by a space): A 1
# Enter the neighbor and its cost (separated by a space): B 4
# Enter the node: A
# Enter the number of neighbors for node A: 2
# Enter the neighbor and its cost (separated by a space): C 3
# Enter the neighbor and its cost (separated by a space): D 2
# Enter the node: B
# Enter the number of neighbors for node B: 1
# Enter the neighbor and its cost (separated by a space): C 5
# Enter the node: C
# Enter the number of neighbors for node C: 1
# Enter the neighbor and its cost (separated by a space): E 5
# Enter the node: D
# Enter the number of neighbors for node D: 0
# Enter the starting node: S
# Enter the goal node: D
# The cost to reach the goal node is: 3



from queue import PriorityQueue

graph = {}

# Prompt the user to input the nodes and their costs
num_nodes = int(input("Enter the number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter the node: ")
    num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))

    neighbors = []
    for _ in range(num_neighbors):
        neighbor, cost = input("Enter the neighbor and its cost (separated by a space): ").split()
        neighbors.append((neighbor, int(cost)))

    graph[node] = neighbors

def uniform_cost_search(start, goal):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    visited = set()

    while not priority_queue.empty():
        cost, current_node = priority_queue.get()

        if current_node == goal:
            return cost

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor not in visited:
                new_cost = cost + neighbor_cost
                priority_queue.put((new_cost, neighbor))

    return -1

start_node = input("Enter the starting node: ")
goal_node = input("Enter the goal node: ")

cost = uniform_cost_search(start_node, goal_node)
if cost == -1:
    print("Goal not found.")
else:
    print(f"The cost to reach the goal node is: {cost}")

# Now the code prompts the user to input the number of nodes, each node, 
# the number of neighbors for each node, and the neighbors along with their costs.
#  This way, the user has full control over the graph structure.
