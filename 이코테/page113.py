import sys
sys.stdin = open('page113.txt')

N = int(input())
cnt = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            # if str(N) in str(k) or str(N) in str(j) or str(N) in str(i):
            if str(N) in str(i) + str(j) + str(k):
                cnt += 1

print(cnt)
