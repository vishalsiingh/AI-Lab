import random
from queue import Queue

def createMaze(rows, cols):
    maze = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    # Make sure start and end positions are free paths (1)
    maze[0][0] = maze[rows-1][cols-1] = 1
    return maze

def printMaze(maze, path=[]):
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in path:
                print("+", end=" ")
            else:
                print(col, end=" ")
        print()

def is_valid(maze, visited, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 1 and not visited[x][y]

def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = Queue()
    queue.put((start, [start])) 
    visited[start[0]][start[1]] = True

    while not queue.empty():
        (x, y), path = queue.get()
        if (x, y) == end:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(maze, visited, nx, ny):
                visited[nx][ny] = True
                queue.put(((nx, ny), path + [(nx, ny)]))

    return None  

# User inputs for the maze size
rows, cols = map(int, input("Enter the number of rows and columns of the maze: ").split())

# Create a random maze
maze = createMaze(rows, cols)

start = tuple(map(int, input("Enter the start position (row, col): ").split()))
end = tuple(map(int, input("Enter the end position (row, col): ").split()))

path = bfs(maze, start, end)

print("Maze:")
printMaze(maze)

if path:
    print("\nPath found:", path)
    print("\nMaze with path:")
    printMaze(maze, path)
else:
    print("\nNo path found!")
