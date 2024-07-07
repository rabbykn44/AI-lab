#Write a program to perform IDDFS traversal on a dynamic graph from user
def iddfs(graph, start_node):
    def dls(node, depth):
        if depth == 0:
            print(node, end=' ')
            return
        if depth > 0:
            for neighbor in graph.get(node, []):
                dls(neighbor, depth - 1)

    depth = 0
    while True:
        print(f"Depth: {depth}", end=' - ')
        dls(start_node, depth)
        print()
        depth += 1

# Input: Adjacency list representation of the graph
# Example input: 0 1 2, 1 3 4, 2 5 6
def input_graph():
    graph = {}
    while True:
        line = input("Enter node and its neighbors (or just press enter to finish): ")
        if line == "":
            break
        parts = list(map(int, line.split()))
        node = parts[0]
        neighbors = parts[1:]
        graph[node] = neighbors
    return graph

if _name_ == "_main_":
    graph = input_graph()
    start_node = int(input("Enter the start node: "))
    iddfs(graph, start_node)