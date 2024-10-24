
def dfs(graph, node, visited):
    visited.add(node) 
    print(node, end=' ')   
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = set()
print("DFS Traversal starting from node A:")
dfs(graph, 'A', visited)
