def binary_search(array, target, start, end):
    if start > end:
        return 'no'
    mid = (start + end) // 2
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1) # 여기 return 안 빼먹게 조심!!
    else:
        return binary_search(array, target, mid + 1, end)


N = int(input())
parts = list(map(int, input().split()))
parts.sort()    # 이진탐색을 위해 정렬 필수!!
M = int(input())
requests = list(map(int, input().split()))
for compo in requests:
    print(binary_search(parts, compo, 0, N - 1), end=" ")
