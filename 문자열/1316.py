import sys
sys.stdin = open('1316.txt')
input = sys.stdin.readline


def group_word_check(word):
    global group_word_cnt
    for i in range(len(word)):
        if i >= 1 and word[i] == word[i - 1]:
            continue
        cnt = word.count(word[i])
        if cnt == 1:
            continue
        start = word.find(word[i])
        end = start + cnt - 1
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