class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.neighbours = []
        self.visited = False

    def add_neighbour(self, vertex):
        self.neighbours.append(vertex)
        return self

    def __str__(self):
        return str(self.value)


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
