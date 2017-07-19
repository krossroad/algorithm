from Graph.Util import Graph
from Graph.BFS import bfs


def run_bfs():
    graph = Graph()

    bfs(graph)


if __name__ == '__main__':
    print "Which app to test?\n1) BFS"

    option = int(raw_input())

    if option == 1:
        run_bfs()
