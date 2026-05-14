# Task 4: Breadth-First Search (BFS) Algorithm

from collections import deque

# Graph representation
# A to E
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["B", "C"],
}


# BFS function
def bfs(graph, start, goal):
    # Start of BFS function
    # Add visited and queue
    visited = []
    queue = deque([[start]])
    # While queue is not empty
    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path
        # if node not in visited
        # add neighbour to queue
        # create new path
        if node not in visited:

            visited.append(node)
            # loop for neighbours of node
            # create new path
            for neighbour in graph[node]:

                new_path = list(path)
                new_path.append(neighbour)

                queue.append(new_path)

    return None
    # End of BFS function


# Run BFS
# A to E
start_node = "A"
goal_node = "E"
# path for A to E
path = bfs(graph, start_node, goal_node)
# print path
print("BFS Search Path:")
print(path)
