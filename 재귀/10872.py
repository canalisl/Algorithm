import sys
sys.stdin = open('10872.txt')


def factorial(n):
    # n이 0일 경우도 고려!!
    if n <= 1:
        return 1
    return n * factorial(n - 1)


N = int(input())
print(factorial(N))