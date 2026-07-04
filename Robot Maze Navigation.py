def dfs(maze, start, goal):
    stack = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            break

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current

    # Reconstruct path
    path = []
    step = goal

    while step is not None:
        path.append(step)
        step = parent.get(step)

    path.reverse()
    return path


def get_neighbors(maze, cell):
    neighbors = []

    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    rows = len(maze)
    cols = len(maze[0])

    for direction in directions:
        neighbor = (
            cell[0] + direction[0],
            cell[1] + direction[1]
        )

        if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
            if maze[neighbor[0]][neighbor[1]] == 0:
                neighbors.append(neighbor)

    return neighbors
