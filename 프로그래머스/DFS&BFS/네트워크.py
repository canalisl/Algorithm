def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            DFS(n, computers, i, visited)
            answer += 1
    return answer

def DFS(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if computers[i][j] == 1 and not visited[j]:
            DFS(n, computers, j, visited)
