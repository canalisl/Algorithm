import sys
sys.stdin = open('1707.txt')
input = sys.stdin.readline


def is_bipartite_graph():
    pass


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    # graph = [[] * (V + 1)]    이건 안됨
    graph = [[] for _ in range(V + 1)]  # 이건 됨
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(graph)