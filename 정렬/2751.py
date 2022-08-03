import sys
sys.stdin = open('2751.txt')
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()
for i in array:
    print(i)