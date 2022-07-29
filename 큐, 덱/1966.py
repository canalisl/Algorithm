from collections import deque
import sys
# sys.stdin = open('1966.txt')
input = sys.stdin.readline


def print_queue(q):
    global order
    q[M] = 0
    print(q)
    while q:
        if q[0] == 0:
            print(order)
            return
        elif q[0] == max(q):
            q.popleft()
            order += 1
        else:
            q.append(q[0])
            q.popleft()


T = int(input())
for _ in range(T):
    order = 1
    N, M = map(int, input().split())
    queue = deque([i for i in map(int, input().split())])
    fakeQ = deque([i for i in range(1, N + 1)])
    print_queue(queue)