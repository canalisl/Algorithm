import sys
sys.stdin = open('1181.txt')
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())
no_same_words = list(set(words))
# 문자열을 사전 순으로 정렬해줌
no_same_words.sort()
# 길이 순으로 정렬
no_same_words.sort(key=len)

for word in no_same_words:
    print(word)