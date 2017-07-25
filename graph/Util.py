import sys
import heapq

from StackQueue.Util import Stack


class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.neighbours = {}
        self.visited = False

    def add_adjacent_vertex(self, edge, vertex):
        self.edges.append(edge)
        return self.add_neighbour(vertex)

    def add_neighbour(self, vertex):
        if vertex.value not in self.neighbours:
            self.neighbours[vertex.value] = vertex

        return self

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value


class DistanceTable(object):
    def __init__(self, vertices):
        #to-do This distance-table initialization could be optimized
        self.vertices = {x: DistanceInfo(x) for x, y in vertices.items()}
        self.queued_vertices = {x: True for x in vertices}
        self.queue = [DistanceInfo(x) for y, x in vertices.items()]

    def pop(self):
        elem = heapq.heappop(self.queue)

        if elem.vertex.value not in self.queued_vertices:
            return self.pop()

        del self.queued_vertices[elem.vertex.value]
        return elem

    def push(self, info):
        key = info.vertex.value

        if key not in self.queued_vertices:
            return None

        if key not in self.vertices:
            self.vertices[key] = info
            heapq.heappush(self.queue, info)
        else:
            if info.min_distance < self.vertices[key].min_distance:
                self.vertices[key] = info
                heapq.heappush(self.queue, info)

    def is_queue_empty(self):
        return len(self.queue) <= 0 or len(self.queued_vertices) <= 0

    def trace_path(self, target_vertex):
        info = self.vertices.get(target_vertex.value)

        if info.predecessor is not None:
            self.trace_path(info.predecessor)

        print "->" + info.vertex.value


class DistanceInfo(object):
    def __init__(self, vertex, min_distance=sys.maxint, predecessor=None):
        self.vertex = vertex
        self.min_distance = min_distance
        self.predecessor = predecessor

    def __lt__(self, other):
        return self.min_distance < other.min_distance

    def __cmp__(self, other):
        return cmp(self.min_distance, other.min_distance)


class Edge(object):
    def __init__(self, vertex1, vertex2, weight, is_directed=True):
        self.vertices1 = vertex1
        self.vertices2 = vertex2
        self.weight = weight
        self.is_directed = is_directed

    def get_other(self, vertex):
        return self.vertices2 if self.vertices1 == vertex else self.vertices1


class Graph(object):
    def __init__(self, is_directed=True):
        self.edges = []
        self.vertices = {}
        self.is_directed = is_directed

    def add_edge(self, edge):
        self.edges.append(edge)
        return self

    def add_edge_raw(self, index1, index2, weight):
        if index1 in self.vertices:
            vertex1 = self.vertices.get(index1)
        else:
            vertex1 = Vertex(index1)
            self.vertices[index1] = vertex1

        if index2 in self.vertices:
            vertex2 = self.vertices.get(index2)
        else:
            vertex2 = Vertex(index2)
            self.vertices[index2] = vertex2

        edge = Edge(vertex1, vertex2, weight)

        self.add_edge(edge)
        vertex1.add_adjacent_vertex(edge, vertex2)
        if not self.is_directed:
            vertex2.add_adjacent_vertex(edge, vertex1)

        return self
