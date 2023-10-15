def dfs(graph,start,visited):
    if visited==None:
        visited=[]
    visited.append(start)
    print(start,end=' ')
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph,neighbour,visited)
    return visited

'''adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(adj_list, 'A',None)'''


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
dfs(adj_list,start_node,None)