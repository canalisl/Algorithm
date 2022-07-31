# 계수정렬 소스코드 직접 구현해보기

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * 10

for num in array:
    count[num] += 1

for i in range(len(count)):
    for _ in range(count[i]):
        print(i, end=" ")