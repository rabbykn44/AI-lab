#Write a program to perform IDDFS traversal on a dynamic graph from user.

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def iddfs(self, start, target, max_depth):
        for depth in range(max_depth):
            visited = set()
            if self.dfs(start, target, depth, visited):
                return True
        return False

    def dfs(self, node, target, depth, visited):
        if depth == 0 and node == target:
            return True
        if depth > 0:
            visited.add(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited and self.dfs(neighbor, target, depth - 1, visited):
                    return True
        return False

def main():
    graph = Graph()

    # Input the number of nodes and edges
    num_nodes = int(input("Enter the number of nodes: "))
    num_edges = int(input("Enter the number of edges: "))

    # Input edges
    print("Enter the edges (source destination):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    # Input start and target nodes
    start_node = int(input("Enter the start node: "))
    target_node = int(input("Enter the target node: "))

    # Set maximum depth for IDDFS
    max_depth = int(input("Enter the maximum depth: "))

    if graph.iddfs(start_node, target_node, max_depth):
        print("Target node is reachable from the start node within maximum depth.")
    else:
        print("Target node is not reachable from the start node within maximum depth.")

if __name__ == "__main__":
    main()

# Enter the number of nodes: 6
# Enter the number of edges: 5
# Enter the edges (source destination):
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# Enter the start node: 1
# Enter the target node: 6
# Enter the maximum depth: 2
