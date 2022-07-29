from collections import deque
import sys
sys.stdin = open('1966.txt')
input = sys.stdin.readline


def print_queue():
    global order, M
    while queue:
        # 중요도 최댓값 저장
        highest = max(queue)
        # 가장 앞의 값 뽑아서 저장
        front = queue.popleft()
        # front 뽑았으므로 타겟 인덱스 앞으로 한 칸 이동
        M -= 1
        # 뽑은게 최댓값이라면
        if front == highest:
            # 인쇄 진행하므로 순서 +1
            order += 1
            # M이 -1이라면 인쇄한게 내 타겟이라는 뜻
            if M < 0:
                # 순서 출력 후 종료
                return order
        # 뽑은게 최댓값이 아니라면
        else:
            # 큐의 뒤에 추가
            queue.append(front)
            # 타겟이 뽑힌 경우
            if M < 0:
                # 타겟 인덱스 제일 뒤로 이동
                M = len(queue) - 1
        

T = int(input())
for _ in range(T):
    # 인쇄 순서 초기화
    order = 0
    N, M = map(int, input().split())
    queue = deque([i for i in map(int, input().split())])
    print(print_queue())