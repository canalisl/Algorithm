def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    numbers.sort(key=lambda x: x.count('0'))
    for i in numbers:
        answer += i
    return answer