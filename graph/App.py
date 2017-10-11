from graph.Dijkstra import calculate_shortest_path
from graph.Util import Vertex, Graph
from graph.BFS import bfs
from graph.DFS import dfs


def run_dijkstra():
    print 'Dijkstra\'s algorithm.'
    graph = Graph()
    graph.add_edge_raw('A', 'C', 8) \
        .add_edge_raw('A', 'B', 2) \
        .add_edge_raw('B', 'D', 10) \
        .add_edge_raw('D', 'C', 1) \
        .add_edge_raw('D', 'E', 1) \
        .add_edge_raw('C', 'E', 8)
    calculate_shortest_path(graph, graph.vertices['A'], graph.vertices['E'])


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


def run_kruksal():
    pass


def run_dfs():
    vertex1 = Vertex(2)
    vertex2 = Vertex(5)
    vertex3 = Vertex(7)
    vertex4 = Vertex(11)
    vertex5 = Vertex(21)

    vertex1.add_neighbour(vertex2)
    vertex1.add_neighbour(vertex4)
    vertex4.add_neighbour(vertex5)
    vertex2.add_neighbour(vertex3)

    dfs(vertex1)


if __name__ == '__main__':
    def wrapper():
        print "Which algorithm to test?"
        print "1) BFS"
        print "2) DFS"
        print "3) Dijkstra's Shortest Path"
        print "4) Kruksal's Minimum Spanning Tree"

        try:
            option = int(raw_input())
        except Exception:
            option = -1

        if option == 1:
            run_bfs()

        elif option == 2:
            run_dfs()

        elif option == 3:
            run_dijkstra()

        elif option == 4:
            run_kruksal()

        else:
            print "Invalid option selected!!"
            wrapper()


    wrapper()
