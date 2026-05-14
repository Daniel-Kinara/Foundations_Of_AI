from collections import deque

# Graph representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"],
}


# BFS function
def bfs(graph, start, goal):

    visited = []
    queue = deque([[start]])

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:

            visited.append(node)

            for neighbour in graph[node]:

                new_path = list(path)
                new_path.append(neighbour)

                queue.append(new_path)

    return None


# Run BFS
start_node = "A"
goal_node = "E"

path = bfs(graph, start_node, goal_node)

print("BFS Search Path:")
print(path)
