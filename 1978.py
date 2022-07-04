import sys
sys.stdin = open('1978.txt')
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
prime = []

for num in numbers:
    for i in range(1, num + 1):
        if (i != 1 and i != num) and num % i == 0:
             numbers.remove(num)
             break

print(len(numbers))