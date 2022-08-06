import sys
sys.stdin = open('11650.txt')
input = sys.stdin.readline

N = int(input())
coor = []
for _ in range(N):
    x, y = map(int, input().split())
    coor.append((x, y))
# 각 요소의 첫번째 원소로 정렬, 같은 경우 두번째 원소로 정렬
coor.sort(key=lambda x: (x[0], x[1]))
# 기본 sort() 메서드도 같은 기능
# coor.sort()
for x, y in coor:
    print(x, y)