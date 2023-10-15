def bfs(graph,start,visited=[],queue=[]):
    visited.append(start)
    queue.append(start)
    while queue:
        m = queue.pop(0)
        print(m, end=' ')
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

'''adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(adj_list, 'A')'''

adj_list={}
key,values='',[]
n=int(input("total no.of nodes:"))
for i in range(n):
    node_value=input("enter the value of the node:")
    if i==0:
        start_node=node_value
    key=node_value
    values=[]
    neighbours=int(input("enter no.of neighbours for the node:"))
    for i in range(neighbours):
        neighbour_value=input("enter neighbour values:")
        values.append(neighbour_value)
        g={key:values}
        adj_list.update(g)
bfs(adj_list,start_node)