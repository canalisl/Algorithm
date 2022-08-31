from itertools import permutations

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    data = permutations(numbers, len(numbers))
    result = [int(''.join(i)) for i in data]
    answer = str(max(result))
    return answer