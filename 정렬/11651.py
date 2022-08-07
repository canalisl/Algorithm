import sys
sys.stdin = open('11651.txt')
input = sys.stdin.readline

N = int(input())
coor = []
for _ in range(N):
    x, y = map(int, input().split())
    coor.append((x, y))

coor.sort(key=lambda x:(x[1], x[0]))
for x, y in coor:
    print(x, y)
