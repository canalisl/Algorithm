def solution(array, commands):
    answer = []
    for i, j, k in commands:
        part = sorted(array[i - 1:j])
        answer.append(part[k - 1])
    return answer