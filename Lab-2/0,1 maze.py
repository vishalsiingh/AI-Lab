from queue import Queue

def createMaze():
    # Representing the maze as a 3x3 grid
    # 0 -> Wall, 1 -> Path
    maze = [
        [1, 0, 1],
        [1, 1, 1],
        [0, 1, 1]
    ]
    return maze

def printMaze(maze, path=[]):
    # Print the maze with the path marked
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in path:
                print("+", end=" ")
            else:
                print(col, end=" ")
        print()

def is_valid(maze, visited, x, y):
    # Check if the cell is within bounds, is a path (1), and not visited
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1 and not visited[x][y]

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = Queue()
    queue.put((start, [start]))  # Queue stores (current_position, path_taken)
    visited[start[0]][start[1]] = True

    while not queue.empty():
        (x, y), path = queue.get()

        # If we reach the end, return the path
        if (x, y) == end:
            return path

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(maze, visited, nx, ny):
                visited[nx][ny] = True
                queue.put(((nx, ny), path + [(nx, ny)]))

    return None  # No path found

# Main execution
maze = createMaze()
start = (0, 0)  # Start position (row, col)
end = (2, 2)    # End position (row, col)

path = bfs(maze, start, end)

print("Maze:")
printMaze(maze)

if path:
    print("\nPath found:", path)
    print("\nMaze with path:")
    printMaze(maze, path)
else:
    print("\nNo path found!")
