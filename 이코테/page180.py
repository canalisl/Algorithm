import sys
sys.stdin = open('page180.txt')
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
    info = input().split()
    array.append((info[0], int(info[1])))
array.sort(key=lambda x: x[1])
for tup in array:
    print(tup[0], end=" ")

