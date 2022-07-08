import sys
sys.stdin = open('page110.txt')

N = int(input())
move = input().split()

x, y = 1, 1



# 문제 잘 읽자!!! 좌우방향이 y좌표 증감 / 상하방향이 x좌표 증감임!!
# L > R > U > D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
direction = ['L', 'R', 'U', 'D']


for movement in move:
    for i in range(len(direction)):
        if movement == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > N or ny < 1 or ny > N:
        continue
    x, y = nx, ny

print(x, y)



        
