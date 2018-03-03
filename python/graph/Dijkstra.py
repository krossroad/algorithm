from graph.Util import DistanceInfo, DistanceTable


def calculate_shortest_path(graph, starting_vertex, target_vertex):
    queue = []

    distance_table = DistanceTable(graph.vertices)
    info = DistanceInfo(starting_vertex, 0)  # set starting vertex as 0

    distance_table.push(info)

    while not distance_table.is_queue_empty():
        current = distance_table.pop()

        for edge in current.vertex.edges:
            adjacent_vertex = edge.get_other(current.vertex)
            distance = current.min_distance + edge.weight

            distance_table.push(DistanceInfo(adjacent_vertex, distance, current.vertex))

    distance_table.trace_path(target_vertex)
