import sys
sys.stdin = open('1316.txt')
input = sys.stdin.readline

# cnt = 0
# words = []
# N = int(input())
# for _ in range(N):
#     words.append(input().rstrip())

# for word in words:
#     for i in range(len(word)):
#         # a의 첫번째 인덱스 + (a의 갯수 - 1) 에 해당하는 인덱스도 a여야지만 불연속적인 a가 없는 것
#         # ex. 'aabbbccb'에서 b의 첫번째 인덱스 2 + b의 갯수 4 - 1 = 5번 인덱스도 b여야지 b가 다 붙어있는 것
#         if word[word.find(word[i]) + word.count(word[i]) - 1] != word[i]:
#             # 그룹단어가 아닌 것 발견하면 1 추가
#             cnt += 1
#             break

# # 전체 단어에서 그룹단어 아닌 것 제외하고 출력
# print(N - cnt)

N=int(input())
count=0
for _ in range(N):
    word=input().rstrip()
    error=0
    for t in range(len(word)-1):
        if word[t] != word[t+1]:
            new_word=word[t+1:]
            if new_word.count(word[t]) > 0:
                error=1
    if error == 0:
        count+=1
print(count)