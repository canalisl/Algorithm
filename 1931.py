import sys
sys.stdin = open('1931.txt')

N = int(input())
meeting = []
cnt = 1

for _ in range(N):
  meeting.append(list(map(int, input().split())))

# 튜플의 첫 번째 요소로 정렬 후, 같은 경우에만 두 번째 요소로 정렬
meeting.sort(key=lambda x: (x[1], x[0]))
# meeting = sorted(meeting, key=lambda x:x[1])
# print("1", meeting)
# meeting = sorted(meeting, key=lambda x:x[0]) 
# print("2", meeting)
endtime = meeting[0][1]
for i in range(1, N):
    if meeting[i][0] >= endtime:
        cnt += 1
        endtime = meeting[i][1]
# print(meeting)
print(cnt)