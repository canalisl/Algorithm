# 이코테 page182 <정렬> 실전문제
import sys
sys.stdin = open('page182.txt')
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B, reverse=True)
for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break
print(sum(A))