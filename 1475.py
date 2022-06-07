import sys
sys.stdin = open('1475.txt')

N = list(input())
cnt = [0] * 10

for i in range(len(N)):
    cnt[int(N[i])] += 1

total = (cnt[6] + cnt[9]) // 2 + (cnt[6] + cnt[9]) % 2
cnt.pop(9)
cnt.pop(6)


for num in cnt:
    if num > total:
        total = num

print(total)