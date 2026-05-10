from queue import PriorityQueue

# Graph structure
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"D": 2, "E": 5},
    "C": {"F": 3},
    "D": {},
    "E": {"F": 1},
    "F": {},
}

# Heuristic values
heuristic = {"A": 7, "B": 6, "C": 2, "D": 1, "E": 1, "F": 0}


# A* Algorithm
def astar(graph, heuristic, start, goal):

    queue = PriorityQueue()
    queue.put((0, start))

    came_from = {}
    cost_so_far = {}

    came_from[start] = None
    cost_so_far[start] = 0

    while not queue.empty():

        current = queue.get()[1]

        if current == goal:
            break

        for neighbour in graph[current]:

            new_cost = cost_so_far[current] + graph[current][neighbour]

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:

                cost_so_far[neighbour] = new_cost

                priority = new_cost + heuristic[neighbour]

                queue.put((priority, neighbour))

                came_from[neighbour] = current

    # Reconstruct path
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()

    return path


# Run algorithm
start_node = "A"
goal_node = "F"

path = astar(graph, heuristic, start_node, goal_node)

print("Optimal Path:")
print(path)
