import sys
sys.stdin = open('2750.txt')

before_sorted_list = []
N = int(input())
for _ in range(N):
    before_sorted_list.append(int(input()))


after_sorted_list = sorted(before_sorted_list)
for i in range(N):
    print(after_sorted_list[i])
