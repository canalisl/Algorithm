import sys
sys.stdin = open('1157.txt')
input = sys.stdin.readline


def findsameletter(word):
    letter_cnt = []
    new_word = list(set(word))
    for letter in new_word:
        letter_cnt.append(word.count(letter))
    if letter_cnt.count(max(letter_cnt)) > 1:
        print('?')
    else:
        print(new_word[letter_cnt.index(max(letter_cnt))])
    # 시간초과
    # max_count = 0
    # max_letter = []
    # for letter in word:
    #     if word.count(letter) == max_count and letter not in max_letter:
    #         max_letter.append(letter)
    #     elif word.count(letter) > max_count:
    #         max_letter = []
    #         max_count = word.count(letter)
    #         max_letter.append(letter)
    # if len(max_letter) > 1:
    #     print('?')
    # else:
    #     print(max_letter[0])


word = input().rstrip().upper()
findsameletter(word)