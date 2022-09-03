import sys
sys.stdin = open('2231.txt')
input = sys.stdin.readline

N = int(input())
result = [num for num in range(1, N) if num + sum(map(int, list(str(num)))) == N]
if len(result) == 0:
    print(0)
else:
    print(min(result))
