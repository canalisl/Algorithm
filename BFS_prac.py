from collections import deque




def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        visited[node] = 1
        print(node, end=' ')
        for i in range(len(graph[start])):
            if not visited[graph[start][i]]:
                queue.append(graph[start][i])
        
visited = [0] * 9

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

bfs(graph, 1, visited)