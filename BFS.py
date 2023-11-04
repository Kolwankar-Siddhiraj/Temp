graph = {
    'A': ['D', 'F'],
    'B': ['F', 'E'],
    'C': ['D', 'F'],
    'D': ['A', 'C'],
    'E': ['F', 'B'],
    'F': ['B', 'C'],
}

visited = []  # List for visited nodes.
queue = []  # Initialize a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:  # Creating a loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')
