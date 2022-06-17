# page. 152 미로 탈출
from collections import deque
import sys
sys.stdin = open('BFS_page152.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
y, x = 0, 0
queue = deque([maze[y][x]])

def bfs(y, x):
    if 


print(queue)