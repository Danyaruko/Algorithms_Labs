class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, start, end, weight):
        edge = [start, end, weight]
        self.edges.append(edge)

    def kruskals_algorithm(self):
        self.edges.sort(key=lambda edge: edge[2])
        print(self.edges)
        min_spanning_tree = list()
        min_spanning_tree_vertices = set()
        for edge in self.edges:
            if edge[0] not in min_spanning_tree_vertices or edge[1] not in min_spanning_tree_vertices:
                min_spanning_tree_vertices.add(
                    edge[0])
                min_spanning_tree_vertices.add(
                    edge[1])
                min_spanning_tree.append(edge)
        return min_spanning_tree


if __name__ == "__main__":
    test_graph = Graph()
    test_graph.add_edge(0, 1, 4)
    test_graph.add_edge(0, 2, 4)
    test_graph.add_edge(1, 2, 2)
    test_graph.add_edge(1, 0, 4)
    test_graph.add_edge(2, 0, 4)
    test_graph.add_edge(2, 1, 2)
    test_graph.add_edge(2, 3, 3)
    test_graph.add_edge(2, 5, 2)
    test_graph.add_edge(2, 4, 4)
    test_graph.add_edge(3, 2, 3)
    test_graph.add_edge(3, 4, 3)
    test_graph.add_edge(4, 2, 4)
    test_graph.add_edge(4, 3, 3)
    test_graph.add_edge(5, 2, 2)
    test_graph.add_edge(5, 4, 3)

    print(test_graph.kruskals_algorithm())
