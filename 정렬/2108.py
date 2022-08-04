import sys
sys.stdin = open('2108.txt')
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]
array.sort()
# 산술평균
print(round(sum(array)/N))

# 중앙값
print(array[N // 2])

# 최빈값
counts = dict()
for i in range(1, N + 1):
    counts[i] = []  # {1: [], 2: [], 3: [], 4: [], 5: []}   1개 있는거 xx, 2개 있는거 xx, ...
max_count = 1
count = 1
if N == 1:  # 입력값이 1개라면
    counts[1].append(array[0])  # 그냥 바로 추가
else:   # 2개 이상이라면
    for j in range(1, N):
        if array[j] == array[j - 1]:  # 직전값과 같을 때는
            count += 1  # 그 숫자개수 +1
        else:   # 새로운 숫자 등장하면
            counts[count].append(array[j - 1])  # 그 직전까지 카운트 한 값 딕셔너리에 추가
            if count > max_count:   # max값보다 크면 max 갱신
                max_count = count
            count = 1   # 새로운 숫자 나왔으므로 카운트 초기화
        if j == N - 1:  # 마지막 값에 도달하면
            counts[count].append(array[j])  # 무조건 딕셔너리에 추가
            if count > max_count:
                max_count = count
if len(counts[max_count]) == 1:
    print(counts[max_count][0])
else:
    counts[max_count].sort()
    print(counts[max_count][1])

# 범위
print(array[-1] - array[0])