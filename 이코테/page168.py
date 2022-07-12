# 퀵 정렬 소스코드 직접 구현해보기 - 1. 정석 방식
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quicksort(array, start, end):
    # 배열의 길이가 1개이면 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 왼쪽부터 피벗보다 큰 값 나오거나 or 끝에 도달할 때까지 탐색 시작
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽부터 피벗보다 작은 값 나오거나 or 시작점(피벗 전)에 도달할 때까지 탐색 시작
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 교차하면 피벗과 작은 값 교환
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 교차 아니면 왼쪽과 오른쪽 값 교환
        else:
            array[left], array[right] = array[right], array[left]
    quicksort(array, start, right - 1)
    quicksort(array, right + 1, end)
    


quicksort(array, 0, len(array) - 1)
print(array)