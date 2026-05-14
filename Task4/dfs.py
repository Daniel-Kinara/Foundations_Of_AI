# Graph representation
# A to E

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"],
}


# DFS function
# Add path if None
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    # add start node to path
    path.append(start)

    if start == goal:
        return path
    # loop for neighbours of start
    for neighbour in graph[start]:
        # if neighbour not in path
        if neighbour not in path:
            # create new path
            result = dfs(graph, neighbour, goal, path.copy())

            if result:
                return result

    return None


# Run DFS
start_node = "A"
goal_node = "E"
# Path from A to E
path = dfs(graph, start_node, goal_node)

# print path
print("DFS Search Path:")
print(path)
