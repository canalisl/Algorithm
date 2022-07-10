# 삽입정렬 소스코드 직접 구현해보기

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        # 왼쪽으로 한칸씩 이동하면서 자기보다 작은 값 나올 때까지 두 개씩 비교
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
        # 자기보다 작은 숫자 만나면 멈추고 다음 숫자로 넘어감
        else:
            break
print(array)