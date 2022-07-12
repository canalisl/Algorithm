# 퀵 정렬 소스코드 직접 구현해보기 - 2. 파이썬 특화 방식
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quicksort_python(array):
    # 배열이 하나 이하의 원소만 갖고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]    # 피벗은 첫 원소
    tail = array[1:]    # 그 나머지가 tail

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quicksort_python(left) + [pivot] + quicksort_python(right)

print(quicksort_python(array))
