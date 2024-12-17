# graph = {
#   '5' : ['3','7'],
#   '3' : ['2', '4'],
#   '7' : ['8'],
#   '2' : [],
#   '4' : ['8'],
#   '8' : []
# }

# visited = set() 

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbours = input(f"Enter the neighbors of {node} separated by spaces: ").split()
        graph[node] = neighbours
    return graph

visited=set()

graph = input_graph()
start_node = input("Enter the starting node for DFS: ")
print("Following is the Depth-First Search:")
dfs(visited, graph, start_node)
# print("Following is the Depth-First Search")
# dfs(visited, graph, '5')