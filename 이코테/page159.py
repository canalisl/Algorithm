# 선택정렬 소스코드 직접 구현해보기

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     # 최솟값의 인덱스
#     min_index = array.index(min(array[i:]))
#     array[i], array[min_index] = array[min_index], array[i]
# print(array)


# min() 안 쓰고 구현
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        # i 뒤의 숫자들 중 최솟값 인덱스 찾기
        if array[j] < array[min_index]:
            min_index = j
    # 최솟값 찾으면 i랑 위치 변경
    array[i], array[min_index] = array[min_index], array[i]
print(array)