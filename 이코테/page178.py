import sys
sys.stdin = open('page178.txt')
input = sys.stdin.readline


N = int(input())
array = [int(input()) for _ in range(N)]
array.sort(reverse=True)
print(*array)