import sys
sys.stdin = open('1181.txt')
input = sys.stdin.readline


def sort_string():
    pass


N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())
print(words)