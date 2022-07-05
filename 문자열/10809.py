import sys
sys.stdin = open('10809.txt')
input = sys.stdin.readline


def findalphabet(word):
    for i in range(ord('a'), ord('z') + 1):
        if chr(i) in word:
            print(word.find(chr(i)), end=" ")
        else:
            print(-1, end=" ")

S = input()
findalphabet(S)