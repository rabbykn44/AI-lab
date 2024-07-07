#  Write a program to perform topological search using IDDFS.
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def iddfs_topological_sort(self, max_depth):
        visited = set()
        topo_order = []
        for node in self.graph:
            if node not in visited:
                if not self.dfs(node, visited, topo_order, max_depth):
                    return "Graph has cycles, topological sorting not possible"
        return topo_order[::-1]

    def dfs(self, node, visited, topo_order, depth):
        if depth == 0:
            return False
        if node in visited:
            return True
        visited.add(node)
        for neighbor in self.graph[node]:
            if not self.dfs(neighbor, visited, topo_order, depth - 1):
                return False
        topo_order.append(node)
        return True

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

    # Set maximum depth for IDDFS
    max_depth = int(input("Enter the maximum depth for IDDFS: "))

    # Perform topological sorting using IDDFS
    sorted_nodes = graph.iddfs_topological_sort(max_depth)

    # Print the topologically sorted nodes
    if isinstance(sorted_nodes, str):
        print(sorted_nodes)
    else:
        print("Topologically sorted nodes:")
        print(sorted_nodes)

if __name__ == "__main__":
    main()
# Enter the number of nodes: 5
# Enter the number of edges: 5
# Enter the edges (source destination):
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5
# Enter the maximum depth for IDDFS: 3
