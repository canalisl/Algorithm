import sys
sys.stdin = open('page115.txt')
input = sys.stdin.readline

N = list(input().rstrip())
alpha = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y = alpha.index(N[0]), int(N[1])
# 우하좌상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

possible = 0

#  우우상, 우우하, 좌좌상, 좌좌하, 상상우, 상상좌, 하하우, 하하좌
for pattern in [(1, 1, 4), (1, 1, 2), (3, 3, 4), (3, 3, 2), (4, 4, 1), (4, 4, 3), (2, 2, 1), (2, 2, 3)]:
    for i in pattern:
        nx = x + dx[i-1]
        ny = y + dy[i-1]
        if nx < 1 or nx > 8 or ny < 1 or ny >8:
            break
        x, y = nx, ny
    if 1 <= nx <= 8 and  1 <= ny <= 8:
        possible += 1
    x, y = alpha.index(N[0]), int(N[1])
    
print(possible)



