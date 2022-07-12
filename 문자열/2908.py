import sys
sys.stdin = open('2908.txt')
input = sys.stdin.readline

A, B = input().split()
reverse_A = A[::-1]
reverse_B = B[::-1]
print(max(int(reverse_A), int(reverse_B)))