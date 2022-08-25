# 효율성테스트 3,4 시간초과
def solution(phone_book):
    answer = True
    for word in phone_book:
        for i in range(len(phone_book)):
            if word != phone_book[i] and word in phone_book[i][:len(word)]:
                answer = False
                return answer
    return answer

# 효율성테스트 3,4 시간초과
# 테스트케이스 실행시간 단축
def solution(phone_book):
    answer = True
    phone_book.sort(key=len)
    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                return answer
    return answer

# 효율성테스트 통과
def solution(phone_book):
    answer = True
    # sort()는 기본적으로 문자열화 된 숫자를 "각 자리별 크기 순서대로" 정렬 / 전체 크기, 길이 X
    # sort(["9", "2365", "23543857395834798", "567", "99999111", "112323", "1"])
    #  -> ['1', '112323', '23543857395834798', '2365', '567', '9', '99999111']
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            return answer
    return answer