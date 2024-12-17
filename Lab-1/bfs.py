# graph={
#     '5':['3','7'],
#     '3':['2','4'],
#     '7':['8'],
#     '2':[],
#     '4':['8'],
#     '8':[],    
# }
# visited=[]
# queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end=" ")
        for neighbour in graph[m]:
         if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbours = input(f"Enter the neighbors of {node} separated by spaces: ").split()
        graph[node] = neighbours
    return graph

# Main execution
visited = []
queue = []

graph = input_graph()
start_node = input("Enter the starting node for BFS: ")
print("The following is the BFS traversal:")
bfs(visited, graph, start_node)
# print(f"The following is the bfs trasversal of is:")     
# bfs(visited,graph,'5')      

 