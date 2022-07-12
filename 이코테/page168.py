# 퀵 정렬 소스코드 직접 구현해보기
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quicksort(array):
    if len(array) == 1:
        return
    pivot = array[0]
    for i in range(1, len(array)):
        # 왼쪽 값이 피벗보다 크고, 오른쪽 값이 피벗보다 작을 때
        if array[i] > pivot and array[-i] < pivot:
            # 단, 왼쪽과 오른쪽이 교차하면
            if i > (len(array) - 1) // 2:
                # 피벗보다 작은 값과 피벗자리 교환
                array[-i], array[0] = array[0], array[-i]
                quicksort(array[:-i])
                quicksort(array[-i + 1:])
            # 자리 교환
            else:
                array[i], array[-i] = array[-i], array[i]


quicksort(array)
print(array)