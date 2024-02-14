# AI-Searching-Algorithms
AI course assignment


# Searching Algorithms in Artificial Intelligence

This repository provides implementations of various searching algorithms used in Artificial Intelligence (AI). Searching algorithms are an essential component of AI systems, enabling the exploration and discovery of solutions in various problem-solving tasks.

## Uninformed Search Algorithms

Uninformed search algorithms are used when there is no available information about the problem domain. These algorithms explore the search space blindly without considering any heuristics or domain-specific knowledge.

### 1. Breadth-First Search (BFS)

Breadth-First Search explores all the neighboring nodes of the current node before moving to the next level of nodes. It guarantees the shortest path to the goal node in terms of the number of edges traversed.

### 2. Depth-First Search (DFS)

Depth-First Search explores the deepest nodes in a branch before backtracking. It does not guarantee the shortest path but is often useful in finding any feasible solution quickly, especially in large search spaces.

### 3. Iterative Deepening Depth-First Search (IDDFS)

Iterative Deepening Depth-First Search combines the benefits of BFS and DFS. It performs multiple DFS searches with increasing depth limits until the goal node is found. This algorithm is memory-efficient and guarantees the optimal solution.

### 4. Uniform Cost Search (UCS)

Uniform Cost Search expands the node with the lowest path cost. It is used when the edges have non-uniform costs and aims to find the lowest-cost path to the goal node.

### 5. Depth-Limited Search (DLS)

Depth-Limited Search is similar to DFS but restricts the depth of the explored nodes to a specified limit. It is useful when the search space is large, and an infinite depth search is not feasible or required.

### 6. Bidirectional Search

Bidirectional Search simultaneously explores the search space from both the initial and goal states. It reduces the search space by converging towards the middle, resulting in a more efficient search.

## Informed Search Algorithms

Informed search algorithms use heuristics or domain-specific knowledge to guide the search process efficiently. These algorithms make use of heuristic functions that estimate the cost or distance to the goal node.

### 1. A* Search

A* Search combines the cost incurred so far (g(n)) and the estimated cost to the goal (h(n)) using a heuristic function to prioritize the nodes for exploration. It guarantees the optimal solution if the heuristic is admissible and consistent.

### 2. Greedy Best-First Search

Greedy Best-First Search selects the node that appears to be closest to the goal based on the heuristic function. It does not consider the cost incurred so far and can be more computationally efficient but may notalways find the optimal solution.

### 3. AO* (Anytime Repairing A*) Algorithm

AO* Algorithm is an informed search algorithm that combines the benefits of A* search and anytime algorithms. It uses a heuristic function to estimate the cost to the goal and incrementally improves the solution over time. AO* provides an anytime property, meaning it can return an improved solution at any time during the search process.

## Usage

Each algorithm is implemented in a separate file within this repository. To use a specific algorithm, follow the instructions provided in the respective file and provide the necessary problem-specific inputs.

## Contributing

Contributions to this repository are welcome. If you would like to contribute an implementation of a searching algorithm or suggest improvements, please open a pull request.


