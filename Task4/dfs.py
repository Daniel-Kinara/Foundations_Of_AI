# Graph representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"],
}


# DFS function
def dfs(graph, start, goal, path=None):

    if path is None:
        path = []

    path.append(start)

    if start == goal:
        return path

    for neighbour in graph[start]:

        if neighbour not in path:

            result = dfs(graph, neighbour, goal, path.copy())

            if result:
                return result

    return None


# Run DFS
start_node = "A"
goal_node = "E"

path = dfs(graph, start_node, goal_node)

print("DFS Search Path:")
print(path)
