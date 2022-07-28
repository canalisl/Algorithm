from collections import deque
import sys
sys.stdin = open('11866.txt')


def josephus_permutation():
    print('<', end="")
    queue = deque([i for i in range(1, N + 1)])
    while queue:
        # 제거할 요소 직전까지를 뽑아서 뒤에 붙이기
        for _ in range(K - 1):
            queue.append(queue[0])
            queue.popleft()
        # 제거한 요소 출력
        print(queue.popleft(), end="")
        # 마지막에는 콤마 출력 안하도록
        if queue:
            print(",", end=" ")
    print('>', end="")
    

N, K = map(int, input().split())
josephus_permutation()