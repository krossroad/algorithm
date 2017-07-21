from graph.Util import Vertex
from graph.BFS import bfs


def run_bfs():
    vertex1 = Vertex(2)
    vertex2 = Vertex(5)
    vertex3 = Vertex(7)
    vertex4 = Vertex(11)
    vertex5 = Vertex(21)

    vertex1.add_neighbour(vertex2)
    vertex1.add_neighbour(vertex4)
    vertex4.add_neighbour(vertex5)
    vertex2.add_neighbour(vertex3)

    bfs(vertex1)


if __name__ == '__main__':
    print "Which app to test?\n1) BFS"

    option = int(raw_input())

    if option == 1:
        run_bfs()
