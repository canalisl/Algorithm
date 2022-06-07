'''
import sys
sys.stdin = open('1026.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
big = dict()
newB = []
newA = [0] * N

# B의 각 원소와 그 원소가 몇 번째로 큰지 매핑
B_small = sorted(B, reverse=True)
for i in range(N):
    big[B_small[i]] = i

# B의 원소가 어떤 크기 순으로 정렬되어 있는지 인덱스로 이루어진 리스트 생성
for num in B:
    for key in big.keys():
        if num == key:
            newB.append(big.get(key))

A_small = sorted(A)

# A를 그와 반대로 정렬
for idx in range(N):
    newA[idx] = A_small[newB[idx]]

S = 0
for i in range(N):
    S += newA[i] * B[i]

print(S)
'''

import sys
sys.stdin = open('1026.txt')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = 0

for i in range(N):
    S += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(S)