import sys
input = sys.stdin.readline


def fib(n):
  global cnt1
  if n == 1 or n == 2:
    cnt1 += 1
    return 1
  else:
    return fib(n - 1) + fib(n - 2)


def fibonacci(n):
  global cnt2
  dp = [0] * (n + 1)
  dp[1], dp[2] = 1, 1
  for i in range(3, n + 1):
    cnt2 += 1
    dp[i] = dp[i - 1] + dp[i - 2]
  return dp[i]

n = int(input())
cnt1, cnt2 = 0, 0
fib(n)
fibonacci(n)
print(cnt1, cnt2)