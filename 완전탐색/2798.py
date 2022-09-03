from itertools import combinations
import sys
sys.stdin = open('2798.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
data = combinations(numbers, 3)
case = [sum(i) for i in data if sum(i) <= M]
print(max(case))