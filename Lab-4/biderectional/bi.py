import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bidirectional_bfs(graph, start, goal):
    """Bi-Directional BFS to find the shortest path."""
    if start == goal:
        return [start], 0, 1  # Path to itself, no edges explored

    # Initialize frontiers and visited sets for both sides
    start_frontier, goal_frontier = {start}, {goal}
    start_visited, goal_visited = {start: None}, {goal: None}
    nodes_explored = 0

    while start_frontier and goal_frontier:
        # Expand the smaller frontier
        if len(start_frontier) <= len(goal_frontier):
            current_side, visited, other_visited, frontier = "start", start_visited, goal_visited, start_frontier
        else:
            current_side, visited, other_visited, frontier = "goal", goal_visited, start_visited, goal_frontier

        # Expand the current frontier
        next_frontier = set()
        for node in frontier:
            nodes_explored += 1
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited[neighbor] = node
                if neighbor in other_visited:  # Path found
                    return reconstruct_path(start, goal, start_visited, goal_visited), len(visited) + len(other_visited), nodes_explored
                next_frontier.add(neighbor)

        # Update the frontier
        if current_side == "start":
            start_frontier = next_frontier
        else:
            goal_frontier = next_frontier

    return None, nodes_explored, nodes_explored  # No path found

def reconstruct_path(start, goal, start_visited, goal_visited):
    """Reconstruct the path from start to goal."""
    path = []
    node = next(iter(set(start_visited) & set(goal_visited)))

    # Build path from start to meeting point
    while node is not None:
        path.append(node)
        node = start_visited[node]
    path.reverse()

    # Build path from meeting point to goal
    node = goal_visited[next(iter(set(start_visited) & set(goal_visited)))]
    while node is not None:
        path.append(node)
        node = goal_visited[node]

    return path

def standard_bfs(graph, start, goal):
    """Standard BFS to find the shortest path."""
    queue = deque([(start, [start])])
    visited = set()
    nodes_explored = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored += 1
        if current == goal:
            return path, nodes_explored
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None, nodes_explored

def dfs(graph, start, goal, path=None, visited=None, nodes_explored=0):
    """Standard DFS to find any path."""
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    nodes_explored += 1

    visited.add(start)
    if start == goal:
        return path, nodes_explored

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, path + [neighbor], visited, nodes_explored)
            if result[0]:
                return result

    return None, nodes_explored

# Visualization Function
def visualize_graph(graph, path=None):
    """Visualize the graph and optionally highlight a path."""
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)

    if path:
        edges_in_path = [(path[i], path[i+1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges_in_path, edge_color="red", width=2)

    plt.show()

# Example Graph (City Map)
city_map = nx.Graph()
city_map.add_edges_from([
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'),
    ('D', 'F'), ('E', 'F'), ('E', 'G'), ('F', 'H'), ('G', 'H')
])

start_node, goal_node = 'A', 'H'

# Bi-Directional BFS
bi_path, bi_nodes, bi_explored = bidirectional_bfs(city_map, start_node, goal_node)
print(f"Bi-Directional BFS: Path = {bi_path}, Nodes Explored = {bi_explored}")

# Standard BFS
bfs_path, bfs_nodes = standard_bfs(city_map, start_node, goal_node)
print(f"Standard BFS: Path = {bfs_path}, Nodes Explored = {bfs_nodes}")

# DFS
dfs_path, dfs_nodes = dfs(city_map, start_node, goal_node)
print(f"DFS: Path = {dfs_path}, Nodes Explored = {dfs_nodes}")

# Visualization
print("\nGraph Visualization:")
visualize_graph(city_map, path=bi_path)