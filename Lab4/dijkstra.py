import heapq


class Edge:
    def __init__(self, end, weight=0):
        if weight < 0:
            raise ValueError

        self.end = end
        self.weight = weight


class Vertice:
    def __init__(self, id, value=None):
        self.id = id
        self.value = value
        self.edges = {}

    def add_edge(self, edge_end, weight):
        self.edges[edge_end.id] = Edge(edge_end, weight)

    def __lt__(self, other):
        return self.id < other.id


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertice(self, vertice):
        self.vertices[vertice.id] = vertice

    def dijkstra_algorithm(self, start_vertice_id):
        distances = {vertice_id: float("inf")
                     for vertice_id in self.vertices.keys()}
        distances[start_vertice_id] = 0
        visited = {vertice_id: False for vertice_id in self.vertices.keys()}
        visited[start_vertice_id] = True

        min_heap = []
        heapq.heappush(min_heap, (0, self.vertices[start_vertice_id]))
        while min_heap:
            cur_vertice = heapq.heappop(min_heap)[1]

            for edge in cur_vertice.edges.values():
                if distances[cur_vertice.id] + edge.weight < distances[edge.end.id]:
                    distances[edge.end.id] = distances[cur_vertice.id] + \
                        edge.weight

                if not visited[edge.end.id]:
                    visited[edge.end.id] = True
                    heapq.heappush(
                        min_heap, (distances[edge.end.id], edge.end))

        return distances


if __name__ == "__main__":
    graph = Graph()
    input_file = open("./input.txt", "r")
    number_of_edges, start_vertice_id = input_file.readline().split()
    number_of_edges = int(number_of_edges)
    for _ in range(number_of_edges):
        edge_start, edge_end, edge_weight = input_file.readline().split()
        edge_weight = int(edge_weight)
        if edge_start not in graph.vertices.keys():
            graph.add_vertice(Vertice(edge_start))
        if edge_end not in graph.vertices.keys():
            graph.add_vertice(Vertice(edge_end))
        graph.vertices[edge_start].add_edge(
            graph.vertices[edge_end], edge_weight)

    distances = [distance for distance in graph.dijkstra_algorithm(
        start_vertice_id).values() if distance != float("inf")]
    print(sum(distances)/(len(distances)-1))
