import sys
sys.stdin = open('1316.txt')
input = sys.stdin.readline


def group_word_check(word):
    global group_word_cnt
    for i in range(len(word)):
        # 연속된 문자면 건너뛰기
        if i >= 1 and word[i] == word[i - 1]:
            continue
        cnt = word.count(word[i])
        # 1개인 문자는 따질 필요 X
        if cnt == 1:
            continue
        start = word.find(word[i])
        end = start + cnt - 1
        # rfind() -> 지정 문자열이 나타나는 '마지막' 위치 반환
        if word.rfind(word[i]) != end:
            return
    else:
        group_word_cnt += 1


N = int(input().rstrip())
group_word_cnt = 0
for _ in range(N):
    word = input().rstrip()
    group_word_check(word)
print(group_word_cnt)