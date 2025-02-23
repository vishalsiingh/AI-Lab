from queue import PriorityQueue

class Puzzle:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal
        self.n = 3

    def find_blank(self, state):
        for i, row in enumerate(state):
            if 0 in row:
                return i, row.index(0)

    def get_neighbors(self, state):
        x, y = self.find_blank(state)
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.n and 0 <= new_y < self.n:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                moves.append(new_state)
        
        return moves

    def manhattan_distance(self, state):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] != 0:
                    goal_x, goal_y = divmod(self.goal.index(state[i][j]), self.n)
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def is_solvable(self, state):
        flat_list = [num for row in state for num in row if num != 0]
        inversions = sum(1 for i in range(len(flat_list)) for j in range(i + 1, len(flat_list)) if flat_list[i] > flat_list[j])
        return inversions % 2 == 0

    def a_star_search(self):
        if not self.is_solvable(self.initial):
            return None

        open_set = PriorityQueue()
        open_set.put((0, self.initial))
        came_from = {}
        g_score = {str(self.initial): 0}
        f_score = {str(self.initial): self.manhattan_distance(self.initial)}

        while not open_set.empty():
            _, current = open_set.get()
            if current == self.goal:
                return self.reconstruct_path(came_from, current)
            
            for neighbor in self.get_neighbors(current):
                neighbor_str = str(neighbor)
                tentative_g_score = g_score[str(current)] + 1
                
                if neighbor_str not in g_score or tentative_g_score < g_score[neighbor_str]:
                    came_from[neighbor_str] = current
                    g_score[neighbor_str] = tentative_g_score
                    f_score[neighbor_str] = tentative_g_score + self.manhattan_distance(neighbor)
                    open_set.put((f_score[neighbor_str], neighbor))
        return None

    def reconstruct_path(self, came_from, current):
        path = []
        while str(current) in came_from:
            path.append(current)
            current = came_from[str(current)]
        return path[::-1]

    def print_puzzle(self, state):
        for row in state:
            print(" ".join(str(cell) if cell != 0 else "_" for cell in row))
        print()

initial_state = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 0]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
]

puzzle = Puzzle(initial_state, goal_state)
solution = puzzle.a_star_search()

if solution:
    for step in solution:
        puzzle.print_puzzle(step)
else:
    print("No solution found! (The puzzle might be unsolvable)")
