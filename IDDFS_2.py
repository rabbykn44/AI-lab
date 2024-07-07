# Write a program to find the path from source to destination using IDDFS.


class IDDFS:
    def __init__(self):
        self.visited = []
        self.path = []

    def iddfs(self, graph, source, destination, max_depth):
        for depth in range(max_depth + 1):
            self.visited = [False] * len(graph)
            self.path = [source]
            if self.dfs(graph, source, destination, depth):
                return True
        return False

    def dfs(self, graph, current, destination, depth):
        if current == destination:
            return True
        if depth <= 0:
            return False

        self.visited[current] = True
        for neighbor in graph[current]:
            if not self.visited[neighbor]:
                self.path.append(neighbor)
                if self.dfs(graph, neighbor, destination, depth - 1):
                    return True
                self.path.pop()
        return False


if __name__ == "__main__":
    try:
        number_of_nodes = int(input("Enter the number of nodes in the graph: "))
        graph = [[] for _ in range(number_of_nodes)]

        print("Enter edges (source destination), press enter after each edge:")
        while True:
            try:
                edge = input().strip()
                if not edge:
                    break
                source, destination = map(int, edge.split())
                graph[source].append(destination)
            except ValueError:
                print("Invalid input format. Please enter source and destination separated by a space.")

        source = int(input("Enter the source node: "))
        destination = int(input("Enter the destination node: "))
        max_depth = int(input("Enter the maximum depth: "))

        iddfs = IDDFS()
        if iddfs.iddfs(graph, source, destination, max_depth):
            print("Path found:", iddfs.path)
        else:
            print("Path not found within the given depth.")
    except ValueError:
        print("Wrong input format.")
    except Exception as e:
        print(f"An error occurred: {e}")
# Enter the number of nodes in the graph: 7
# Enter edges (source destination), press enter after each edge:
# 0 1
# 0 2
# 1 3
# 1 4
# 2 5
# 2 6

# Enter the source node: 0
# Enter the destination node: 6
# Enter the maximum depth: 3
# Path found: [0, 2, 6]