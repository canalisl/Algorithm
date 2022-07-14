import sys
sys.stdin = open('5622.txt')
input = sys.stdin.readline


def word_to_number(word):
    time = 0
    for letter in word:
        if letter in 'ABC':
            time += 3
        elif letter in 'DEF':
            time += 4
        elif letter in 'GHI':
            time += 5
        elif letter in 'JKL':
            time += 6
        elif letter in 'MNO':
            time += 7
        elif letter in 'PQRS':
            time += 8
        elif letter in 'TUV':
            time += 9
        else:
            time += 10
    return time


word = input().rstrip()
print(word_to_number(word))