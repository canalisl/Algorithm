from collections import deque
import sys
sys.stdin = open('2164.txt')
input = sys.stdin.readline


def last_card(n):
    queue = deque()
    for i in range(1, N + 1):
        queue.append(i)
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(*queue)


N = int(input().rstrip())
last_card(N)