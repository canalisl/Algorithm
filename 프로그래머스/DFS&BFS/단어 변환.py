from collections import deque


def solution(begin, target, words):
    answer = 0
    queue = deque(begin)
    while queue:
        now = queue.popleft()
        cnt = 0
        if now == target:
            return answer
        for next in words:
            for i in range(len(next)):
                if now[i] != next[i]:
                    cnt += 1
            if cnt == 1:
                queue.append(next)
                answer += 1
    return 0

