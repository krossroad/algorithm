class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
        self.visited = False


class Edge(object):
    def __init__(self):
        self.vertices = []
