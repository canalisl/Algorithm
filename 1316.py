import sys
sys.stdin = open('1316.txt')
input = sys.stdin.readline

word = []
N = int(input())
for _ in range(N):
    word.append(input().rstrip())

print(N, word)