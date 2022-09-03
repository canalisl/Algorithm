import sys
sys.stdin = open('7568.txt')
input = sys.stdin.readline

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
rating = []
for i in range(len(people)):
    cnt = 0
    for j in range(len(people)):
        if j != i and people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    rating.append(cnt + 1)
print(*rating)