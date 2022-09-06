import sys
sys.stdin = open('2231.txt')
input = sys.stdin.readline

N = int(input())

for num in range(1, N):
    result = num
    temp = num
    while num != 0:
        result += num % 10
        num //= 10
    if result == N:
        print(temp)
        break
else:
    print(0)