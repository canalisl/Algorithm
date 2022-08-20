from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    queue = deque()  # 그냥 begin을 넣으면 문자열 분해돼서 들어감
    queue.append((begin, 0))    # deque([('hit', 0)])
    # queue = deque((begin, 0))   # deque(['hit', 0]) -> popleft하면 'hit'만 나옴
    # queue = deque([(begin, 0)])   # 한 번에 할거면 이렇게
    while queue:
        now, cnt = queue.popleft()
        if now == target:
            return cnt
        cnt += 1
        for i in range(len(words)):    
            diff = 0
            for j in range(len(now)):
                if now[j] != words[i][j]:
                    diff += 1
            if diff == 1:
                queue.append((words[i], cnt))
    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))