def dfs(start):
    for index, neighbor in start.neighbours.items():
        if not neighbor.visited:
            dfs(neighbor)

    start.visited = True
    print start
