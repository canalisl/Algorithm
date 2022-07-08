from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        # 이 때 방문체크하면 늦음! > 이미 다른 노드에서 뻗어나가서 방문한 노드가 또 큐에 추가될 수 있음 ex. 7은 2에서 이미 방문했는데 8에서 또 방문함
        # visited[node] = 1
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                # 인접한 노드를 큐에 추가하는 이 순간 방문체크 해야함
                visited[i] = 1
        
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