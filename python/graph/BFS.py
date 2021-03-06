from StackQueue.Util import Queue


def bfs(start):
    queue = Queue()
    start.visited = True
    queue.enqueue(start)

    while not queue.is_empty():
        vertex = queue.de_queue()
        print vertex

        for index, neighbour in vertex.neighbours.items():
            if neighbour.visited:
                continue

            queue.enqueue(neighbour)
