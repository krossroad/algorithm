class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
        self.visited = False

    def add_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)
        return self


class Edge(object):
    def __init__(self, vertex1, vertex2, weight):
        self.vertices1 = vertex1
        self.vertices2 = vertex2
        self.weight = weight


class Graph(object):
    def __init__(self):
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)
        return self
