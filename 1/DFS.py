# Creating an empty dictionary where we'll store the edges of the graph
graph = {}

# Function to add edges to the graph
def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

# Function to do a depth-first traversal of the graph
def dfs_traversal(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_traversal(graph, neighbor, visited)

# Taking input from the user
n = int(input("Enter the number of edges in the graph: "))
for i in range(1, n+1):
    start, end = input(f"Enter the edge {i} separated by a space (start end): ").split()
    add_edge(graph, start, end)

# Doing a depth-first traversal starting from node 'a'
start_node = input("Enter the starting node for DFS traversal: ")
print("DFS Traversal: ", end="")
dfs_traversal(graph, start_node)
print()
