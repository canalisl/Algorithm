import sys
sys.stdin = open('2675.txt')
input = sys.stdin.readline


def RepeatStr(R, string_list):
    new_word = ''
    for letter in string_list:
        new_word += letter * R
    print(new_word)


T = int(input())
for _ in range(T):
    R, S = input().split()
    RepeatStr(int(R), list(S))

