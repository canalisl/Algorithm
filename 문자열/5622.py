import sys
sys.stdin = open('5622.txt')
input = sys.stdin.readline


def word_to_number(word):
    time = 0
    for letter in word:
        for i in range(len(dial)):
            if letter in dial[i]:
                time += i + 3
                break
    return time


word = input().rstrip()
dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
print(word_to_number(word))