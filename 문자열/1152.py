import sys
sys.stdin = open('1152.txt')
input = sys.stdin.readline

sentence = input().split()
print(len(sentence))